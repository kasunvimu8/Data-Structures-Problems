from data_structures.stack import Stack

class QueueFromStacks:
  def __init__(self):
    self.push_stack = Stack()
    self.pop_stack = Stack()
    
  def is_empty(self):
    return self.push_stack.is_empty() and self.pop_stack.is_empty();

  def enqueue(self, item) :
    self.push_stack.push(item)
  
  def dequeue(self):
    if self.push_stack.is_empty() and self.pop_stack.is_empty() :
      return
    
    if self.pop_stack.is_empty() :
      while not self.push_stack.is_empty() :
        self.pop_stack.push(self.push_stack.pop())
    
    return self.pop_stack.pop()

  def size(self):
    return self.push_stack.size() + self.pop_stack.size()
