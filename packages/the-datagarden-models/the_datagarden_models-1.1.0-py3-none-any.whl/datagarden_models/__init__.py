"""
Module to provide a combined storage and data classes for specified data models.
The classes include pydantic validation of the data and storage of the data via
a selected storage class.


Available methods
'init_database'
    - method to define name and alias for the database
    - if needed host info and credentials can be added to the arguments

>>> configure_database(host="localhost", port=27017, username="user", password="pass")


available Dataclasses
- GeoNameDataClass, data class aimed at storing data from GeoNames website
- RetailLocationsDataClass, data class aimed at storing retail locations

avaialble fieldtypes (to be used to instantiatie specific dataclasses fields)
- PointField


Objects for discovery of available dataclasses
- ALL_MODEL_CLASSES: List with all data models
- ALL_GDG_MODEL_NAMES: List with class_names of all dataclasses.
- model_name_to_model: method to retrieve the actual data class for its name.
"""

from .models import DemographicsV1, DemographicsV1Keys
from .models.base import DataGardenModel


class DatagardenDataModels:
	DEMOGRAPHICS: type[DataGardenModel] = DemographicsV1


class DatagardenDataModelKeys:
	DEMOGRAPHICS: type = DemographicsV1Keys


def get_values_from_class(cls: type):
	for key, value in vars(cls).items():
		if not key.startswith("__"):
			yield value


AVAILABLE_MODELS = [
	klass.DATAGARDEN_MODEL_NAME
	for klass in get_values_from_class(DatagardenDataModelKeys)
]
__all__ = ["DatagardenDataModels", "DatagardenDataModelKeys", "AVAILABLE_MODELS"]
