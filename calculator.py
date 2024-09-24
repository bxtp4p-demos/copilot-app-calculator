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

def main():
    calc = Calculator(0)
    while True:
        print("\nOptions:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Calculate Circle Area")
        print("7. Save History to File")
        print("8. Load History from File")
        print("9. Clear History")
        print("10. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print(f"Result: {calc.add(x, y)}")
        elif choice == '2':
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print(f"Result: {calc.subtract(x, y)}")
        elif choice == '3':
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print(f"Result: {calc.multiply(x, y)}")
        elif choice == '4':
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print(f"Result: {calc.divide(x, y)}")
        elif choice == '5':
            x = float(input("Enter base number: "))
            y = float(input("Enter exponent: "))
            print(f"Result: {calc.power(x, y)}")
        elif choice == '6':
            radius = float(input("Enter radius: "))
            print(f"Result: {calc.calculate_circle_area(radius)}")
        elif choice == '7':
            filename = input("Enter filename to save history: ")
            calc.save_to_file(filename)
            print("History saved.")
        elif choice == '8':
            filename = input("Enter filename to load history: ")
            print("History loaded:")
            print(calc.load_from_file(filename))
        elif choice == '9':
            calc.clear_history()
            print("History cleared.")
        elif choice == '10':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()