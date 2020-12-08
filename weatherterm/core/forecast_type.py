'''
Represents each option of the weather forecast we will provide to the users of our application.
'''

from enum import Enum, unique

@unique
class ForecastType(Enum):
	TODAY = 'today'
	FIVEDAYS = '5day'
	TENDAYS = '10day'
	WEEKEND = 'weekend'