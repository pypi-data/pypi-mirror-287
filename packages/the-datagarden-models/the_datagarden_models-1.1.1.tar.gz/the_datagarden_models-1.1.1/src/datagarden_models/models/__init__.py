from .base import DataGardenModel
from .demographics import DemographicsV1, DemographicsV1Keys
from .economics import EconomicsV1, EconomicsV1Keys


class DatagardenModels:
	DEMOGRAPHICS: type[DataGardenModel] = DemographicsV1
	ECOMOMICS: type[DataGardenModel] = EconomicsV1


class DatagardenModelKeys:
	DEMOGRAPHICS: type = DemographicsV1Keys
	ECOMOMICS: type = EconomicsV1Keys


__all__ = ["DatagardenModels", "DatagardenModelKeys"]
