from pydantic import BaseModel, Field

from .base_economics import EconomicsValue


class GDPV1Legends:
	TOTAL_GDP = "Total GDP value for the region."
	GDP_PER_INHABITANT = "GDP per inhabitant."


L = GDPV1Legends


class GDP(BaseModel):
	total_gpd: EconomicsValue = Field(
		default_factory=EconomicsValue, description=L.TOTAL_GDP
	)
	gpd_per_inhabitant: EconomicsValue = Field(
		default_factory=EconomicsValue, description=L.TOTAL_GDP
	)


class GDPV1Keys:
	TOTAL_GDP = "total_gpd"
	GDP_PER_INHABITANT = "gpd_per_inhabitant"
