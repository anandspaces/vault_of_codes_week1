# Temperature Converter

## Introduction

This project contains a Python function named `convert_temperature` that converts temperatures between Fahrenheit and Celsius. The function is designed to take two arguments: the temperature to convert and the unit of the input temperature ('F' for Fahrenheit, 'C' for Celsius). The function returns the converted temperature rounded to two decimal places.

## Requirements

- Python 3.x

## Function Description

The function `convert_temperature` performs the following conversions:
- If the input unit is 'F' (Fahrenheit), it converts the temperature to Celsius.
- If the input unit is 'C' (Celsius), it converts the temperature to Fahrenheit.

### Conversion Formulae:
- **Celsius to Fahrenheit**: \( (C * \frac{9}{5}) + 32 \)
- **Fahrenheit to Celsius**: \( (F - 32) * \frac{5}{9} \)

### Rounding:
- The result is rounded to 2 decimal places using the `round()` function.

## Conclusion

This function provides a simple way to convert temperatures between Fahrenheit and Celsius, ensuring accuracy by rounding the results to two decimal places. Feel free to use and modify this function as needed for your projects.
