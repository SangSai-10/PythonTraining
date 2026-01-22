# input has exactly three words. ex Python is fun -> fun is Python


def reverse(input_data):
    input_data = input_data.split(" ")
    reversestr1,reversestr2,reversestr3 = input_data
    reversedstr = reversestr3+" "+reversestr2+" "+reversestr1
    return reversedstr


# ----------------------------------------------#
#      Do not modify the test code below        #
# ----------------------------------------------#


def validate(expected, actual):
    assert actual == expected, f"Search -> expected {expected} got {actual}"


result = reverse("Python is fun")
validate(expected="fun is Python", actual=result)

result = reverse("So little time")
validate(expected="time little So", actual=result)

result = reverse("Be the change")
validate(expected="change the Be", actual=result)
