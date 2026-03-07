

input_data = "John,20,2026"
tokens = input_data.split(",")  # ["John", "30", "2026"]
name, age, year = tokens
age = int(age) + 1
year = int(year) + 1

res = ",".join([name, str(age), str(year)])
res = f"{name},{age},{year}"
print(res)