

teamA = {"John", "Dave", "Mike"}
teamB = set()

teamB.add("Bob")
teamB.update(["Charlie", "Robert", "John"])
# # print(len(teamA))

x = teamB.difference(teamA)
print(x)

# x = 6 + 4

# union
all_members = teamA | teamB
print(all_members)

# # intersection
common_a_b = teamA & teamB
print(common_a_b)

# # difference
only_team_a = teamA - teamB
print(only_team_a)

# # symmetric difference
contributes_100 = teamA ^ teamB
print(contributes_100)


# x = set("Hello")
# print(x)

# x.add(2)
# print(x)

# # remove duplicates
numbers = [1, 2, 3, 3, 4, 1]
unique = list(set(numbers))
print(numbers)
print(unique)

set_nums = {1, 2, 3, 4, 5}
nums = {1, 2, 3}

# # sub, super set check
print(nums.issubset(set_nums))
print(set_nums.issuperset(nums))


# # days = {"mon"..."sat" ,"sun"}
# # work_week = { "mon" ... "fri" }

numbers = [4, 2, 3, 1]
numbers.sort()
ordered = sorted(numbers) ### keep original and create a copy]
print(numbers) 
print(ordered)


