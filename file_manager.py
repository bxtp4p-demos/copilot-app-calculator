class FileManager:
    """
    A simple file manager class that supports saving and loading history to a file.
    """

    def __init__(self, filename=None):
        """
        Initializes the file manager with an optional filename.

        :param filename: The name of the file to save/load history to/from.
        """

        self.filename = filename

    def set_filename(self, filename):
        """
        Sets the filename to save/load history to/from.

        :param filename: The name of the file to save/load history to/from.
        """

        self.filename = filename

    def save_to_file(self, history):
        """
        Saves the history to a file.

        :param history: A list of history entries to save.
        """

        if not self.filename:
            raise ValueError("Filename not set.")
        with open(self.filename, 'w') as file:
            file.write("History of calculations:\n")
            for entry in history:
                file.write(entry + "\n")

    def load_from_file(self):
        """
        Loads the history from a file.
        
        :return: A list of history entries.
        """
        
        if not self.filename:
            raise ValueError("Filename not set.")
        with open(self.filename, 'r') as file:
            return file.readlines()

