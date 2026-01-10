age = 15
can_vote = age > 18
print("can vote?:",can_vote)

age = 22
can_vote = age > 18
print("can vote?:",can_vote)

def can_vote(age):
    # res = age > 18
    return age > 18

eligible = can_vote(12)
print("Is eligible to vote?:",eligible)