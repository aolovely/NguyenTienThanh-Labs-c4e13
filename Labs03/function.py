x = float(input("x = "))
operation = input("Operation (+, -, *, /)")
y = float(input("y = "))
def  op(x, y, operation):
    if operation == "+":
        return x + y
    elif operation == "-":
        return x - y
    elif operation == "*":
        return x*y
    else:
        return x/y

print("{0} + {1} = {2}".format(x, y, op(x,y, operation)))
print("* "*8)
