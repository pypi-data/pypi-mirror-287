from pydantic import Field

from ..base import DataGardenModel, DataGardenModelLegends
from .base_health import ByGender, HealthBaseKeys


class HealthV1Keys(
	HealthBaseKeys,
):
	DEATH_RATE_BY_IDC10 = "death_rate_idc10"
	DATAGARDEN_MODEL_NAME = "Health"


class HealthV1Legends(DataGardenModelLegends):
	DEATH_RATE_BY_IDC10 = (
		"Death cause by  IDC10 categorization, see https://icd.who.int/browse10/2010/en"
		" for detailed description of IDC10 categories"
	)


L = HealthV1Legends


class HealthV1(DataGardenModel):
	datagarden_model_version: str = Field(
		"v1.0", frozen=True, description=L.DATAGARDEN_MODEL_VERSION
	)
	death_rate_idc10: ByGender = Field(
		default_factory=ByGender, description=L.DEATH_RATE_BY_IDC10
	)
