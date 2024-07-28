from pydantic import BaseModel, Field


class EconomicValueBaseKeys:
	VALUE = "value"
	UNIT = "unit"
	CURRENCY = "currency"


class EconomicValueBaseLegends:
	VALUE = "value in units of given currency"
	UNIT = "units for value"
	CURRENCY = "currency for value"


L = EconomicValueBaseLegends


class EconomicsValue(BaseModel):
	value: float | None = Field(default=None, description=L.VALUE)
	unit: int = Field(default=1, description=L.UNIT)
	currency: str = Field(default="EUR", description=L.CURRENCY)
