from stack import Stack


class PostfixEvaluator:
    operations = ['+', '-', '/', '*']

    def __init__(self, str):
        self.result = ''
        self.input = str

    def is_operator(self, x):
        return x in self.operations

    def evaluate(self):
        notationInvalid = 'Given Notation is Incorrect !'
        s = Stack()

        for c in self.input:
            if self.is_operator(c):

                if s.size() < 2:
                    return notationInvalid
                val = str(s.pop()) + c + str(s.pop())
                ans = eval(val)
                s.push(ans)

            else:
                s.push(c)

        if s.size() != 1:
            return notationInvalid
        else:
            return s.pop()

# postFixEvaluator = PostfixEvaluator('34+2*1+')
# print(postFixEvaluator.evaluate())
