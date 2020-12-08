'''
Represents the temperature units that the user will be able to choose from in the command line.
'''

from enum import Enum, unique

@unique
class BaseEnum(Enum):
    def _generate_next_value_(name, start, count, last_value):
        '''
        Overrides the method _generate_next_value_ so that every enumeration that inherits from BaseEnum and has properties with the value set to auto() will automatically get the same value as the property name.
        '''

        return name
