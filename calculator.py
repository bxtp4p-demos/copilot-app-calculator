import math

class Calculator:
    def __init__(self, initial_value):
        self.value = initial_value
        self.history = []
        self.result = 0

    def add(self, x, y):
        self.result = x + y
        self.history.append(f"Added {x} to {y} got {self.result}")
        return self.result

    def subtract(self, x, y):
        self.result = x - y
        self.history.append(f"Subtracted {y} from {x} got {self.result}")
        return self.result

    def multiply(self, x, y):
        self.result = x * y
        self.history.append(f"Multiplied {x} with {y} got {self.result}")
        return self.result

    def divide(self, x, y):
        if y == 0:
            print("Cannot divide by zero")
            return None
        self.result = x / y
        self.history.append(f"Divided {x} by {y} got {self.result}")
        return self.result

    def power(self, x, y):
        self.result = math.pow(x, y)
        self.history.append(f"Raised {x} to the power of {y} got {self.result}")
        return self.result

    def calculate_circle_area(self, radius):
        self.result = math.pi * radius * radius
        self.history.append(f"Calculated area of circle with radius {radius} got {self.result}")
        return self.result

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write("History of calculations:\n")
            for entry in self.history:
                file.write(entry + "\n")

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            self.history = file.readlines()
        return self.history

    def clear_history(self):
        self.history = []
        