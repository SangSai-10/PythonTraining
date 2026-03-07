x = 1  # start
# is_greater = X <=10
while x<=10 : #stop
    print (x *2 )
    x = x + 1 #step

print("End")


def table(num):
    while num <= 10:
        # print (num ,"*", 1 ,"=",num*1)
        table_format = f"{num}*2={num*2}"
        print(table_format)
        num = num + 1

table(1)