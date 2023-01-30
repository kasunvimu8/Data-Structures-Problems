from stacks_and_queues.stack import Stack

# check the paranthesis matching


def isOpenningParanthesis(arg):
    switcher = {
        '(': True,
        '{': True,
        '[': True,
        '<': True,
    }
    return switcher.get(arg, False)


def balance_paranthesis_problem(paranthesis):
    stack = Stack()
    for para in paranthesis:
        print(para)

    return paranthesis[4]


balanced = balance_paranthesis_problem("(({}))")
print(balanced)
