![GitHub top language](https://img.shields.io/github/languages/top/Danieltandrade/Unit-Converter)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/unit_converter_python)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/unit-converter-python)
![GitHub License](https://img.shields.io/github/license/Danieltandrade/Unit-Converter)
![PyPI - Version](https://img.shields.io/pypi/v/unit_converter_python)

# Unit Converter

This project is a simple unit converter.
In version 0.0.2 it will be possible to convert units related to distance, pressure, temperature, weight and the new torque and power units.

The package unit-converter-python is used to:
	
 	- Distance conversion:
		- centimeter
		- fathom
		- feet
		- inch
		- kilometer
		- meters
		- mile
		- yard

	- Power conversion:
		- horse power
		- kilowatt
		- metric horse power
		- watt

	- Pressure Conversion:
		- atm
		- bar
		- kgf/m²
		- pascal
		- psi

	- Temperature Conversion:
		- Celsius
		- Fahrenheit
		- Kelvin

	- Torque conversion:
		- kgf.m
		- lbf.ft
		- lbf.in
		- nm

	- Weight Conversion:
		- Gram
		- Kilogram
		- Ounce
		- Pound

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install unit-converter-python

```bash
pip install unit_converter_python
```

## Usage

This package can be used in applications where it is necessary to convert units of measurement.

Here we have an example of use converting a temperature measurement from Fahrenheit to Celsius.

### Step 1
Import the desired package.

```python
from unit_converter_python.temperature import fahrenheit_conversion_to
```

### Step 2
Use the function to convert the value from Fahrenheit to Celsius.

Example:
```python
fahrenheit_value = 62
converted_value = fahrenheit_conversion_to.f_to_c(fahrenheit_value)
print(f"The temperature of {fahrenheit_value}ºF was converted to {converted_value:.2F}ºC.")
```

## Author
Daniel Torres de Andrade

## License
[MIT](https://choosealicense.com/licenses/mit/)
