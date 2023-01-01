from data_structures.stack import Stack

class PostfixEvaluator:
  operations = ['+', '-', '/', '*']

  def __init__(self):
    self.items = []

  def is_operation(x):
    return x in operations


  