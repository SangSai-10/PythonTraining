def sum(a,b):
    c = a + b
    print("")
    return c
a=10
b=20
c = sum(a,b)
print("sum of a,b ",c)

def add(x,y):
    z = x + y
    print("Sum of X,Y =",z)


add(2,3)

def sub(x,y):
    z = x - y
    print("Diff of X,Y =",z)

sub(9,7)

def sub(x,y):
    # z = x - y
    # print("Diff of X,Y =",z)
    return x-y

a = 5
b = 3
z = sub(a,b)
print("Value returned :",z)

def multiply(x,y):
    z = x * y
    print("Value within function : ",z)
    return z

multiply(10,20)
d = multiply(2,3)
print("Value returned from fn : ",d)


def truediv(x,y):
    z = x / y
    print("Value within function : ",z)
    return z

truediv(30,10)
d = truediv(9,3)
print("Value returned from fn : ",d)


def mod(x,y):
    z = x % y
    print("Value within function : ",z)
    return z

mod(29,5)
d = mod(5,2)
print("Value returned from fn : ",d)

def flrdiv(x,y):
    z = x // y
    print("Value within function : ",z)
    return z

flrdiv(29,5)
d = flrdiv(3,2)
print("Value returned from fn : ",d)