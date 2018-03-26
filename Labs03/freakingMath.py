from random import randint
from random import choice
from eval import op

x = randint(1, 10)
y = randint(1, 10)
er = [-1, 0, 1]
er1 = choice(er)
ops = ["+", "-", "*", "/"]
op1 = choice(ops)
total = op(x, y, op1)
res =total + er1

print("{0} {1} {2} = {3}".format(x, op1, y, res))

s = input("(Y/N) ").upper()

if res == total and s =="Y":
        print("Yep")
elif res != total and s == "N":
        print ("Yep")
else:
        print("wrong")
