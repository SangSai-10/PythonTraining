# email_dict = {}

# def add(datadict, key, value):
#     datadict.update({key: value})
# add(email_dict, "Name", "John V")
# add(email_dict, "Phone", "+1 234-567-898")

# print(email_dict)


# contacts_list = [
#     ["Alice Johnson", "+1 234-567-890"],
#     ["Bob Martin", "555 123 4567"],
#     ["Charlie", "(416) 987-6543"]
#     ]

# email_dict = {}
# for user in contacts_list:
#     name, phone = user
#     email_dict.update({email: user})
    # user_map[email] = name

email_dict = {}

# def add(datadict, key, value):
#     datadict.update({key: value})

contacts_list = [
    ["Alice Johnson", "+1 234-567-890"],
    ["alice Johnson", "+1 234-567-890"],
    ["Bob Martin", "555 123 4567"],
    ["Charlie", "(416) 987-6543"]
]

# # Update dictionary using your add() function
# for name, phone in contacts_list:
#     add(email_dict, name, phone)

# print(email_dict)

def is_valid_phone(phone):
    for ch in phone:
        if ch.isdigit() or ch == " " or ch == "+" or ch == "-" or ch == "(" or ch == ")":
            return True
        else:
            return False
# def duplicate_name(name):     
    

def add_contact(datadict, key, value):
    # Check duplicates (case-insensitive)
    for name_already_exist in datadict:
        if name_already_exist.upper() == key.upper():
            print("Duplicate name not allowed:", key)
            return
    # datadict[key] = value
    datadict.update({key: value})

for name, phone in contacts_list:
    add_contact(email_dict, name, phone)


for name, phone in email_dict.items():
         if is_valid_phone(phone):
          print(name, ": VALID PHONENUMBER")
         else:
            print(name, ": INVALID PHONENUMBER")

print(email_dict)

# -----------------------------------------***********************---------------------------------------
for key, value in email_dict.items():
     print(f"{key},{value}")

def search_partialcontacts(datadict,search_item):
    search_item = search_item.lower()
    results = []

    for name in datadict:
        if search_item in name.lower():         
            results.append((name, datadict.get(name)))  # using get()

    return results

match_found = search_partialcontacts(email_dict,"Al")
print(match_found)


def delete(datadict,name):
    datadict.pop(name)

delete = delete(email_dict,"Bob Martin")
print(email_dict)

