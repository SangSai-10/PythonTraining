# ********1***************
def firstten_num(n):
    while n <= 10:
        print (n)
        n = n + 1
n = 1
firstten_num(n)
# ********2***************

def firstten_num(n):
    while n <= 10:
        print (n * 2)
        n = n + 1
n = 1
firstten_num(n)
# ********3***************

def table(num):
    while num <= 10:
        # print (num ,"*", 1 ,"=",num*1)
        table_format = f"{num}*2={num*2}"
        print(table_format)
        num = num + 1
num = 1
table(num)

# # ********4***************
def table(num):
    while num <= 10:
        print(num)
        num = num + 2
num = 1
table(num)


# # ********5***************
def table(num):
    while num <= 10:
        if num % 3 == 0:
            print(num)
        num = num +1
        
num = 1
table(num)


# # ********6***************
def table(stop):
    num=1
    while num <= stop:
        if num % 3 == 0 and num % 5 == 0:
            print(num)
        num = num +1
        
table(50)
# ********7***************
def table(num):
    sum = 1
    newtotal = 0
    while sum <= num:
    #    res = sum + 1
       newtotal = newtotal + sum
       sum = sum + 1
    print(newtotal)  

         
num = 4
table(num)


# ********8***************
def table(num):
    sum = 1
    newtotal = 1
    while sum <= num:
    #    res = sum + 1
       newtotal = newtotal * sum
       sum = sum + 1
    print(newtotal)  

         
num = 5
table(num)


