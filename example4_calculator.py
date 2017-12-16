def add(x, y):
    result = x + y
    return result


def mult(x, y):
    result = x * y
    return result

print "1. Add"
print "2. Multiply"
action = raw_input("Pick a number: ")

a = raw_input("First number: ")
a = float(a)
b = raw_input("Second number: ")
b = float(b)

if action == "1":
    result = add(a,b)
elif action == "2":
    result = mult(a,b)
else:
    result = "Error"

print "Answer: %s" % result


