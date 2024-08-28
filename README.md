# Calculator App

## Overview

`Calculator.py` is a Python module that implements a simple calculator class, `Calculator`, designed to perform basic arithmetic operations, calculate power and area of a circle, and manage a history of calculations. This module is ideal for educational purposes, simple mathematical operations, and as a base for more complex calculator applications.

This module is primarily used in conjunction with prompt engineering exercises and demos. It is not intended for production use.

## Features

The `Calculator` class supports the following operations:

- **Addition (`add`):** Adds two numbers and returns the result.
- **Subtraction (`subtract`):** Subtracts the second number from the first and returns the result.
- **Multiplication (`multiply`):** Multiplies two numbers and returns the result.
- **Division (`divide`):** Divides the first number by the second. If the second number is zero, it prints "Cannot divide by zero" and returns None.
- **Power (`power`):** Raises the first number to the power of the second number and returns the result.
- **Calculate Circle Area (`calculate_circle_area`):** Calculates the area of a circle given its radius and returns the result.
- **Save to File (`save_to_file`):** Saves the history of calculations to a specified file.
- **Load from File (`load_from_file`):** Loads a history of calculations from a specified file.
- **Clear History (`clear_history`):** Clears the history of calculations.

## Usage Example

```python
from calculator import Calculator

calc = Calculator(0)
print(calc.add(10, 5))  # 15
print(calc.subtract(10, 5))  # 5
print(calc.multiply(10, 5))  # 50
print(calc.divide(10, 2))  # 5.0
print(calc.power(2, 3))  # 8.0
print(calc.calculate_circle_area(5))  # 78.53981633974483
calc.save_to_file('history.txt')
calc.clear_history()
print(calc.load_from_file('history.txt')) 
```

You can test this example by running the following command:

```bash
python example.py
```

## Dependencies

- Python 3.x
- math module (standard library)

## Installation

No installation is required beyond having Python 3.x installed on your system. Simply download calculator.py and include it in your project.

## Virtual Environment

You can use virtual environments to manage dependencies and isolate your project environment. To create a virtual environment, run the following commands:

```bash
python3 -m venv venv
source venv/bin/activate
```

then run the following command to install the dependencies:

```bash
pip install -r requirements.txt
```

## Testing

To run the example usage file, execute the following command:

```bash
python3 example.py
```

## Contribution

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.
