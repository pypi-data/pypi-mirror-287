from .base import DataGardenModel
from .demographics import DemographicsV1, DemographicsV1Keys
from .economics import EconomicsV1, EconomicsV1Keys


class DefaultAppModels:
	DEMOGRAPHICS: type[DataGardenModel] = DemographicsV1
	ECOMOMICS: type[DataGardenModel] = EconomicsV1


__all__ = ["DemographicsV1Keys", "EconomicsV1Keys", "DefaultAppModels"]
