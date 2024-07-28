from typing import Any

from lightning import LightningModule
from torch.nn import Module, BCELoss
from torch.optim import Optimizer, AdamW
from torchmetrics.classification import BinaryAccuracy, BinaryAUROC
from typing_extensions import Self

from qusi.internal.logging import get_metric_name


class QusiLightningModule(LightningModule):
    @classmethod
    def new(
            cls,
            model: Module,
            optimizer: Optimizer | None,
            loss_metric: Module | None = None,
            logging_metrics: list[Module] | None = None,
    ) -> Self:
        if optimizer is None:
            optimizer = AdamW(model.parameters())
        if loss_metric is None:
            loss_metric = BCELoss()
        if logging_metrics is None:
            logging_metrics = [BinaryAccuracy(), BinaryAUROC()]
        instance = cls(model=model, optimizer=optimizer, loss_metric=loss_metric,
                       logging_metrics=logging_metrics)
        return instance

    def __init__(
            self,
            model: Module,
            optimizer: Optimizer,
            loss_metric: Module,
            logging_metrics: list[Module],
    ):
        super().__init__()
        self.model: Module = model
        self._optimizer: Optimizer = optimizer
        self.loss_metric: Module = loss_metric
        self.logging_metrics: list[Module] = logging_metrics

    def forward(self, inputs: Any, target: Any) -> Any:
        return self.model(inputs, target)

    def training_step(self, batch: tuple[Any, Any], batch_index: int):
        inputs, target = batch
        predicted = self(inputs, target)
        loss = self.loss_metric(predicted, target)
        for logging_metric in self.logging_metrics:
            logging_metric_value = logging_metric(predicted, target)
            logging_metric_name = get_metric_name(logging_metric)
            self.log(name=logging_metric_name, value=logging_metric_value, on_step=False, on_epoch=True)
        return loss

    def configure_optimizers(self):
        return self._optimizer
