from random import *
from eval import val
def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(1, 10)
    y = randint(1, 10)
    er = choice([-1, 0, 1])
    ops = ["+", "-", "*", "/"]
    operation = choice(ops)
    res = val(x, y, operation) + er
    return [x, y, operation, res]

def check_answer(x, y, op, result, user_choice):
    if user_choice == True and result == val(x, y, op):
        return True
    if user_choice == False and result != val(x, y, op):
        return True
    return False
