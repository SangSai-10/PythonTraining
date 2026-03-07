
# message = "scala, F# pattern matching, deconstruction"
# index = message.find("match")
# print(index)

source_data ="Learning Python is fun"
search_term = "fun"


def search_position(source_data, search_term):
    search = source_data.find(search_term)
    return search


excer = "John,20,2026"
excer = excer.split(",")
str1,str2,str3 = excer
print(str1)
str2 = int(str2)+ 1
print(str2)
str3 = int(str3)+1
print(str3)

# b= f"{str1},{str2},{str3}"
b = str1 +","+str(str2)+","+str(str3)
print(b)


def reve():
   result = "Python is fun"
   result = result.split(" ")
   reversestr1,reversestr2,reversestr3 = result
   reversedstr = reversestr3+" "+reversestr2+" "+reversestr1
   print(reversedstr)
    
reve()


message = "Hello World"
print(message)

message = message.upper()
print(message)

message = message.title()
print(message)

data = "John,30,IT,34958"  # CSV
print(data)
tokens = data.split(",")
print(tokens)


sentence = "-".join(tokens)
print(sentence)

message = "scala, F# pattern matching, deconstruction"

starts_with = message.startswith("scala")
print(starts_with)

ends_with = message.endswith("deconstruction")
print(ends_with)

op = "xxxxHelloxxxWorldxxx"
# op = op.strip()

op = op.lstrip("x")

# op = op.lower().strip("x")
print(op)



