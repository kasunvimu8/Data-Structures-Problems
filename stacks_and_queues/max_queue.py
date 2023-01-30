from stack import Stack

# special stack which returnning the maxinmum vlaue in the stack


class Maxstack:
    def __init__(self):
        self.stack = Stack()
        self.max_stack = Stack()

    def is_empty(self):
        return self.stack.is_empty()

    def push(self, item):
        if self.max_stack.is_empty():
            max_val = item - 1
        else:
            max_val = self.max_stack.peek()

        if item > max_val:
            self.max_stack.push(item)

        self.stack.push(item)

    def pop(self):
        if self.stack.is_empty() or self.max_stack.is_empty():
            return

        pop_item = self.stack.pop()

        if pop_item == self.max_stack.peek():
            self.max_stack.pop()

        return pop_item

    def max(self):
        if self.stack.is_empty() or self.max_stack.is_empty():
            return 'No Items Found !'
        else:
            return self.max_stack.pop()

    def size(self):
        return self.stack.size()
