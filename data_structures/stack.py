class Stack:
  def __init__(self):
    self.items = []
    
  def is_empty(self):
    return self.items == []

  def push(self, item):
    self.items.append(item)
    
  def pop(self):
    return self.items.pop()

  def peek(self):
    # or self.items[-1]
    if len(self.items) > 0 :
      return self.items[len(self.items) -1]
    else:
      return None

  def size(self):
    return len(self.items)
