class HistoryManager:
    """
    A class to manage the history of operations.
    """

    def __init__(self):
        """
        Initializes the history manager with an empty history.
        """
        self.history = []

    def add_entry(self, operation, *args, result):
        """
        Adds an entry to the history of operations.

        :param operation: The name of the operation.
        :param args: The arguments for the operation.
        :param result: The result of the operation.
        """

        operands = ", ".join(map(str, args))
        self.history.append(f"{operation}({operands}) = {result}")

    def clear_history(self):
        """
        Clears the history of operations.
        """

        self.history = []

    def get_history(self):
        """
        Returns the history of operations.
        
        :return: A list of history entries.
        """
        return self.history