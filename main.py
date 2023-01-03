from data_structures.stack import Stack

class InfixToPostFix:
    operations = ['+', '-', '/', '*', '(', ')']

    def __init__(self, str):
      self.result = ''
      self.input = str

    def is_operator(self, x):
      return x in self.operations

    def check_precedence(self, operator):
      switcher = {
        '+' : 1,
        '-' : 1,
        '*' : 2,
        '/' : 2,
      }
      return switcher.get(operator, -1)

    def is_closing_operator(self, operator):
      return operator == ')'
    def is_opening_operator(self, operator):
      return operator == '('
  
    def convert(self):
      s = Stack()
      out = ''

      for c in self.input:
        if self.is_operator(c):
          if self.is_closing_operator(c):
            i = 0
            while i < s.size():
              item = s.pop()
              if self.is_opening_operator(item):
                break;
              out+=str(item)
          else:
            top_operator = s.peek();
            if self.check_precedence(top_operator) < self.check_precedence(c):
               s.push(c)
            else:
              out+=str(s.pop())
              s.push(c)
        else:
          out+=str(c)

      if s.size() != 1:
        return ('Given Notation is Incorrect !')
      else:
        return s.pop()
        
convert_to_postfix = InfixToPostFix('(3+4)*2+1')
print(convert_to_postfix.convert())


# class Stack(list):
#     push = list.append
#     peek = lambda self: self[-1]