from datetime import datetime

class HistoryEntry:
   """
   A simple class to represent an entry in the history of calculations.
   """

   def __init__(self, message):
      """
      Initializes the history entry with a message and the current timestamp.

      :param message: The message to store in the history entry.
      """
      
      self.message = message
      self.timestamp = datetime.now()

   def __repr__(self):
      """
      Returns a string representation of the history entry.

      :return: A string representation of the history entry.
      """

      return f"{self.timestamp}: {self.message}"