num=1
for i in range(1,11,1):
    table_format = f"{i} * {num} = {i* num}"
    print(table_format)

sum = 0
for i in range(1,5,1):
    sum = sum + i
print(sum)

message = "Hello World"

# fin = message.find("W")
# print(fin)
size = len(message)
position = -1
for i in range(0,size,1):
    if message[i] == "W":
       position = i

print(position)

# format = f"W found in index {i}"
# print(format)



     
