def multiply(x, y):
    z = x
    for i in range(y-1):
        z = z+x
    return z

result = multiply(10, 10)
print(result)

def exponent(x, y):
    z = x
    for i in range(y-1):
        z = z*x
    return z

result = exponent(3, 3)
print(result)

def square(x):
   return exponent(x, 2)

result = square(9)
print(result)