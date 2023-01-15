from data_structures.stack import Stack

class QueueFromStacks:

    def __init__(self, str):
      self.push_stack = Stack()
      self.pop_stack = Stack()
      
    def is_empty(self):
      return self.push_stack == [] and self.pop_stack == [];

    # def enqueue(self, item) :
    #   self.items.insert(0, item)
    
    # def dequeue(self):
    #   return self.items.pop();

    def size(self):
      return len(self.push_stack) + len(self.pop_stack)
    
        
queue = QueueFromStacks();
# queue.is_empty()
# queue.enqueue(2)
# queue.dequeue()
# queue.size()
