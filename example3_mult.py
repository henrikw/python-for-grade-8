import time
print "Multiply"


def mult(x, y):
    print "Hmmm..."
    time.sleep(3)  # Wait 3 seconds
    print "Multiplying %s and %s" % (x, y)  # Print two values - requires brackets around x and y.
    result = x * y
    return result

a = raw_input("First number: ")
a = int(a)
b = raw_input("Second number: ")
b = int(b)
result = mult(a, b)
print "Result: %s" % result
