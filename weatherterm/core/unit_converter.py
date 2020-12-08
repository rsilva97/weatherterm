from .unit import Unit


class UnitConverter:
	def __init__(self, parser_default_unit, dest_unit=None):
		'''
		This is the class that is going to make the temperature conversions from Celsius to Fahrenheit and vice versa. The initializer of this class gets two arguments; the default unit used by the parser and the destination unit. In the initializer, we will define a dictionary containing the functions that will be used for temperature unit conversion.
		'''
		self._parser_default_unit = parser_default_unit
		self._dest_unit = dest_unit

		self._convert_functions = {
			Unit.CELSIUS: self._to_celsius,
			Unit.FAHRENHEIT: self._to_fahrenheit,
		}

	@property
	def dest_unit(self):
		return self._dest_unit

	@dest_unit.setter
	def dest_unit(self, dest_unit):
		self._dest_unit = dest_unit

	def convert(self, temp):

		try:
			temperature = float(temp)
		except ValueError:
			return 0

		if (self.dest_unit == self._parser_default_unit or
				self.dest_unit is None):
			return self._format_results(temperature)

		func = self._convert_functions[self.dest_unit]
		result = func(temperature)

		return self._format_results(result)

	def _format_results(self, value):
		return int(value) if value.is_integer() else f'{value:.1f}'

	def _to_celsius(self, fahrenheit_temp):
		result = (fahrenheit_temp - 32) * 5/9
		return result

	def _to_fahrenheit(self, celsius_temp):
		result = (celsius_temp * 9/5) + 32
		return result
	