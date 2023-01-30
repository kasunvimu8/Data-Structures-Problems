from stacks_and_queues.stack import Stack

# check the paranthesis matching, important for compilers

def is_balance_paranthesis(arg1, arg2):
  if ((arg1 == '(' and arg2 == ')') or
      (arg1 == '{' and arg2 == '}') or
      (arg1 == '[' and arg2 == ']') or
      (arg1 == '<' and arg2 == '>')):
    return True
  else:
    return False
  

def is_openning_paranthesis(arg):
  switcher = {
      '(': True,
      '{': True,
      '[': True,
      '<': True,
  }
  return switcher.get(arg, False)


def balance_paranthesis_problem(paranthesis):
  stack = Stack()
  status = True

  for para in paranthesis:
    if is_openning_paranthesis(para):
      stack.push(para)
    else:
      if stack.is_empty():
        status = False
        break
      else:
        if is_balance_paranthesis(stack.pop(), para):
          continue
        else:
          status = False
          break
  return status


balanced = balance_paranthesis_problem("(({?}[][]))")
print(balanced)
