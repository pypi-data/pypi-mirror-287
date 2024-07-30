"""This module provides a Multimodal Ensemble model for GeoLifeCLEF2024 data.

Author: Lukas Picek <lukas.picek@inria.fr>
        Theo Larcher <theo.larcher@inria.fr>

License: GPLv3
Python version: 3.10.6
"""
from typing import Any, Callable, Mapping, Optional, Union

import numpy as np
import omegaconf
import torch
from omegaconf import OmegaConf
from torch import Tensor, nn
from torch.optim.lr_scheduler import CosineAnnealingLR
from torchmetrics import Metric
from torchvision import models

from malpolon.models import ClassificationSystem

from .utils import check_optimizer


class TopK(Metric):
    def __init__(self, k: int, num_labels: int, dist_sync_on_step=False):
        super().__init__(dist_sync_on_step=dist_sync_on_step)
        self.k = k
        self.num_labels = num_labels
        self.add_state("top_k_correct", default=torch.tensor(0.0), dist_reduce_fx="sum")
        self.add_state("total_top_k", default=torch.tensor(0.0), dist_reduce_fx="sum")

class TopKPrecision(TopK):
    def __init__(self, k: int, num_labels: int, dist_sync_on_step=False):
        super().__init__(k, num_labels, dist_sync_on_step=dist_sync_on_step)

    def update(self, preds: torch.Tensor, target: torch.Tensor):
        # Assuming preds are logits
        top_k_preds = torch.topk(preds, self.k, dim=1).indices
        for i in range(preds.size(0)):
            top_k_set = set(top_k_preds[i].tolist())
            targets_1 = torch.nonzero(target[i], as_tuple=False).squeeze().tolist()
            if np.isscalar(targets_1):  # happens when the tensor passed to torch.tolist() contains only 1 value
                targets_1 = [targets_1]
            target_set = set(targets_1)
            correct_predictions = len(top_k_set & target_set)
            self.top_k_correct += correct_predictions
            self.total_top_k += self.k

    def compute(self):
        return self.top_k_correct / self.total_top_k

class TopKRecall(TopK):
    def __init__(self, k: int, num_labels: int, dist_sync_on_step=False):
        super().__init__(k, num_labels, dist_sync_on_step=dist_sync_on_step)

    def update(self, preds: torch.Tensor, target: torch.Tensor):
        # Assuming preds are logits
        top_k_preds = torch.topk(preds, self.k, dim=1).indices
        for i in range(preds.size(0)):
            top_k_set = set(top_k_preds[i].tolist())
            targets_1 = torch.nonzero(target[i], as_tuple=False).squeeze().tolist()
            if np.isscalar(targets_1):  # happens when the tensor passed to torch.tolist() contains only 1 value
                targets_1 = [targets_1]
            target_set = set(targets_1)
            correct_predictions = len(top_k_set & target_set)
            actual_positives = len(target_set)

            self.top_k_correct += correct_predictions
            self.total_actual_positives += actual_positives

    def compute(self):
        return self.top_k_correct / self.total_actual_positives


class ClassificationSystemGLC24(ClassificationSystem):
    """Classification task class for GLC24_pre-extracted.

    Inherits ClassificationSystem.
    """
    def __init__(
        self,
        model: Union[torch.nn.Module, Mapping],
        lr: float = 1e-2,
        weight_decay: float = 0,
        momentum: float = 0.9,
        nesterov: bool = True,
        metrics: Optional[dict[str, Callable]] = None,
        task: str = 'classification_binary',
        loss_kwargs: Optional[dict] = {},
        hparams_preprocess: bool = True
    ):
        if isinstance(loss_kwargs, omegaconf.dictconfig.DictConfig):
            loss_kwargs = OmegaConf.to_container(loss_kwargs, resolve=True)
        if 'pos_weight' in loss_kwargs.keys():
            length = metrics['multilabel_f1-score'].kwargs.num_labels
            loss_kwargs['pos_weight'] = Tensor([loss_kwargs['pos_weight']] * length)
        super().__init__(model, lr, weight_decay, momentum, nesterov, metrics, task, loss_kwargs, hparams_preprocess)
        optimizer = torch.optim.AdamW(model.parameters(), lr=lr)
        self.optimizer = check_optimizer(optimizer)

    def configure_optimizers(self):
        scheduler = CosineAnnealingLR(self.optimizer, T_max=25, verbose=True)
        res = {'optimizer': self.optimizer,
               'lr_scheduler': scheduler}
        return res


    def forward(self, x, y, z):  # noqa: D102 pylint: disable=C0116
        return self.model(x, y, z)

    def _step(
        self, split: str, batch: tuple[Any, Any], batch_idx: int
    ) -> Union[Tensor, dict[str, Any]]:
        if split == "train":
            log_kwargs = {"on_step": True, "on_epoch": True, "sync_dist": True}
        else:
            log_kwargs = {"on_step": True, "on_epoch": True, "sync_dist": True}

        x_landsat, x_bioclim, x_sentinel, y, survey_id = batch
        y_hat = self(x_landsat, x_bioclim, x_sentinel)

        pos_weight = y * self.model.positive_weigh_factor
        self.loss.pos_weight = pos_weight  # Proper way would be to forward pos_weight to loss instantiation via loss_kwargs, but pos_weight must be a tensor, i.e. have access to y -> Not possible in Malpolon as datamodule and optimizer instantiations are separate

        loss = self.loss(y_hat, self._cast_type_to_loss(y))  # Shape mismatch for binary: need to 'y = y.unsqueeze(1)' (or use .reshape(2)) to cast from [2] to [2,1] and cast y to float with .float()
        self.log(f"loss/{split}", loss, **log_kwargs)

        metric = TopKPrecision(k=25, num_labels=len(y[0]))
        metric.update(y_hat, y)
        score = metric.compute()
        # print(f"Top-{25} Precision: {precision:.4f}")
        self.log(f"Multilabel_precision_top25/{split}", score, **log_kwargs)

        for metric_name, metric_func in self.metrics.items():
            if isinstance(metric_func, dict):
                score = metric_func['callable'](y_hat, y, **metric_func['kwargs'])
            else:
                score = metric_func(y_hat, y)
            self.log(f"{metric_name}/{split}", score, **log_kwargs)

        return loss

    def predict_step(self, batch, batch_idx, dataloader_idx=0):  # noqa: D102 pylint: disable=C0116
        x_landsat, x_bioclim, x_sentinel, y, survey_id = batch
        print(f"Survey ID: {survey_id}")
        return self(x_landsat, x_bioclim, x_sentinel)


class MultimodalEnsemble(nn.Module):
    """Multimodal ensemble model processing Sentinel-2A, Landsat & Bioclimatic data.

    Inherits torch nn.Module.
    """
    def __init__(self, num_classes=11255, positive_weigh_factor=1.0, **kwargs):
        super().__init__(**kwargs)
        self.positive_weigh_factor = positive_weigh_factor

        self.landsat_model = models.resnet18(weights=None)
        self.landsat_norm = nn.LayerNorm([6, 4, 21])
        # Modify the first convolutional layer to accept 6 channels instead of 3
        self.landsat_model.conv1 = nn.Conv2d(6, 64, kernel_size=3, stride=1, padding=1, bias=False)
        self.landsat_model.maxpool = nn.Identity()

        self.bioclim_model = models.resnet18(weights=None)
        self.bioclim_norm = nn.LayerNorm([4, 19, 12])
        # Modify the first convolutional layer to accept 4 channels instead of 3
        self.bioclim_model.conv1 = nn.Conv2d(4, 64, kernel_size=3, stride=1, padding=1, bias=False)
        self.bioclim_model.maxpool = nn.Identity()

        self.sentinel_model = models.swin_t(weights="IMAGENET1K_V1")
        # Modify the first layer to accept 4 channels instead of 3
        self.sentinel_model.features[0][0] = nn.Conv2d(4, 96, kernel_size=(4, 4), stride=(4, 4))
        self.sentinel_model.head = nn.Identity()

        self.ln1 = nn.LayerNorm(1000)
        self.ln2 = nn.LayerNorm(1000)
        self.fc1 = nn.Linear(2768, 4096)
        self.fc2 = nn.Linear(4096, num_classes)

        self.dropout = nn.Dropout(p=0.1)

    def forward(self, x, y, z):  # noqa: D102 pylint: disable=C0116
        x = self.landsat_norm(x)
        x = self.landsat_model(x)
        x = self.ln1(x)

        y = self.bioclim_norm(y)
        y = self.bioclim_model(y)
        y = self.ln2(y)

        z = self.sentinel_model(z)

        xyz = torch.cat((x, y, z), dim=1)
        xyz = self.fc1(xyz)
        xyz = self.dropout(xyz)
        out = self.fc2(xyz)
        return out
