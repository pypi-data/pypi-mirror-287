from .demographics import DemographicsV1, DemographicsV1Keys
from .economics import EconomicsV1, EconomicsV1Keys


class DatagardenModels:
	DEMOGRAPHICS = DemographicsV1
	ECOMOMICS = EconomicsV1


class DatagardenModelKeys:
	DEMOGRAPHICS = DemographicsV1Keys
	ECOMOMICS = EconomicsV1Keys


__all__ = ["DatagardenModels", "DatagardenModelKeys"]
