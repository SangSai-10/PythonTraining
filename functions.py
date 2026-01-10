def say_hello():
    print("Hello Sangee")


say_hello()

def user_name():
    name = input("Enter user name: ")
    print(name)


def user_age():
    age = input("Enter user age: ")
    print(age)
    age = int(age)
    print(type(age))
    # print(type(int(age)))


# user_name()
user_age()


x = 10
y = 5
z = x-y
print("Result of z",z)

def sub():
    x = 20
    y = 9
    z = x%y
    print("Result of z in fn",z)

sub()

# +, -, *, /, //, %