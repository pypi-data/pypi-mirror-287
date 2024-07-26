from .base import DataGardenModel
from .demographics import DemographicsV1, DemographicsV1Keys


class DefaultAppModels:
	DEMOGRAPHICS: type[DataGardenModel] = DemographicsV1


__all__ = ["DemographicsV1Keys", "DemographicsV1", "DefaultAppModels"]
