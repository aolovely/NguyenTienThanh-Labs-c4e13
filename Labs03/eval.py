from random import randint
from random import choice
#
# x = 3
# y = 7
# total = -1
# op = ["+", "-", "*", "/"]
# op1 = choice(op)
#
# if op1 == "+":
#     total =  x + y
# elif op1 == "-":
#     total = x - y
# elif op1 == "*":
#     total = x * y
# else:
#     total = int(x/y)
#
# print(total)
#
# def love1(x, y):
#     total = -1
#     op = ["+", "-", "*", "/"]
#     op1 = choice(op)
#
#     if op1 == "+":
#         total =  x + y
#     elif op1 == "-":
#         total = x - y
#     elif op1 == "*":
#         total = x * y
#     else:
#         total = int(x/y)
#     print(total)
#
# love1(8, 9)
#
# operation = ["+"]
def  op(x, y, operation):
    if operation == "+":
        return x + y
    elif operation == "-":
        return x - y
    elif operation == "*":
        return x*y
    else:
        return x/y
#
# re = op(10, 5, "+")
# print(re)
