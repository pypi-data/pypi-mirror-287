from pydantic import Field

from ..base import DataGardenModel

# from .base_demographics import DemographicsBaseKeys
from .gdp import GDP, GDPV1Keys


class EconomicsV1Keys(GDPV1Keys):
	GDP = "gdp"
	DATAGARDEN_MODEL_NAME = "Economics"



class EconomicsV1Legends:
	GDP = "Gross Domestic Product"
	DATAGARDEN_MODEL_VERSION = "Version of the data model."


L = EconomicsV1Legends


class EconomicsV1(DataGardenModel):
	datagarden_model_version: str = Field(
		"v1.0", frozen=True, description=L.DATAGARDEN_MODEL_VERSION
	)
	gdp: GDP = Field(default_factory=GDP, description=L.GDP)
