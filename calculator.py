import math
from history_entry import HistoryEntry
from history_manager import HistoryManager
from file_manager import FileManager


class Calculator:
    """
    A simple calculator class that supports basic arithmetic operations,
    power calculation, and area calculation for a circle. It utilizes a
    history manager to log all operations.
    """

    def __init__(self, history_manager=None, pow_func=math.pow, pi_value=math.pi):
        """
        Initializes the calculator with optional custom power function,
        pi value, and a history manager.
        
        :param history_manager: An instance of HistoryManager to log operations.
        :param pow_func: A function to calculate power.
        :param pi_value: The value of pi to use in calculations.
        """
        
        self.result = 0
        self.history_manager = history_manager or HistoryManager()
        self.pow_func = pow_func
        self.pi_value = pi_value

    def _execute_operation(self, operation_name, func, *args):
        """
        Executes a given arithmetic operation and logs it to the history.
        
        :param operation_name: The name of the operation.
        :param func: The function to execute for the operation.
        :param args: The arguments for the operation function.
        :return: The result of the operation.
        """

        try:
            self.result = func(*args)
            self.history_manager.add_entry(operation_name, *args, result=self.result)
        except ZeroDivisionError:
            self.result = "Error: Cannot divide by zero"
            self.history_manager.add_entry(operation_name, *args, result=self.result)
            raise # Re-raise the exception
        return self.result

    def add(self, x, y):
        """
        Adds two numbers and logs the operation.
        
        :param x: The first number.
        :param y: The second number.
        :return: The result of the addition.
        """
        
        return self._execute_operation("add", lambda x, y: x + y, x, y)

    def subtract(self, x, y):
        """
        Subtracts two numbers and logs the operation.

        :param x: The first number.
        :param y: The second number.
        :return: The result of the subtraction.
        """

        return self._execute_operation("subtract", lambda x, y: x - y, x, y)

    def multiply(self, x, y):
        """
        Multiplies two numbers and logs the operation.

        :param x: The first number.
        :param y: The second number.
        :return: The result of the multiplication.
        """

        return self._execute_operation("multiply", lambda x, y: x * y, x, y)

    def divide(self, x, y):
        """
        Divides two numbers and logs the operation.

        :param x: The first number.
        :param y: The second number.
        :return: The result of the division.
        """

        
        return self._execute_operation("divide", lambda x, y: x / y, x, y)

    def power(self, x, y):
        """
        Raises a number to the power of another number and logs the operation.

        :param x: The base number.
        :param y: The exponent number.
        :return: The result of the power operation.
        """

        return self._execute_operation("power", self.pow_func, x, y)

    def calculate_circle_area(self, radius):
        """
        Calculates the area of a circle with a given radius and logs the operation.

        :param radius: The radius of the circle.
        :return: The result of the area calculation.
        """

        if radius < 0:
            raise TypeError("Radius cannot be negative")

        return self._execute_operation("calculate_circle_area", lambda r: self.pi_value * r * r, radius)