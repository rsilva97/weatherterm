from enum import Enum, unique
from .base_enum import BaseEnum

@unique
class Unit(Enum):
	'''
	Every property is set to auto(), meaning the value for every item in the enumeration will be set automatically for us.
	'''

	CELSIUS = auto()
	FAHRENHEIT = auto()