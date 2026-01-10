# Given age check if user can vote ex age>18
def can_vote(age):
    result = age > 18
    return result

age = 15 
eligible_to_vote  = can_vote(age)
print(" User eligible to vote:?" , eligible_to_vote)

age = 20
eligible_to_vote  = can_vote(age)
print(" User eligible to vote:?" , eligible_to_vote)
print("_______________________________________________")

# Given age check if user can drive 
def drive(age,has_license):
    result = age > 18 and has_license == True
    return result

age = 15 
has_license = True
eligible_to_drive  = drive(age,has_license)
print(" User eligible to drive:?" ,eligible_to_drive)

age = 20
has_license = True
eligible_to_drive = drive(age,has_license)
print(" User eligible to drive:?" ,eligible_to_drive)
print("_______________________________________________")

# Given score check
#  whether candidate passed, failed, scored centum

def student_score(marks):
    pass_fail = marks >= 35
    return pass_fail

marks = 40
exam_result = student_score(marks)
print("Student score pass mark:?", exam_result)

def student_score(marks):
    pass_fail = marks < 34
    return pass_fail

marks = 25
exam_result = student_score(marks)
print("Student score fail mark:?", exam_result)
print("_______________________________________________")

def centum(marks):
    full_mark = marks == 100
    return full_mark

score = 100
testscore = centum(score)
print("Has student scored centum in exam:?",testscore)
print("_______________________________________________")

# Given body temperature check if user has fever(more than 100)
def can_vacinate(temp):
    fever = temp >= 100
    return fever
temp = 95
eligible_for_shot = can_vacinate(temp)
print("Eligible for shot:? ", not eligible_for_shot)

# Given username, password check whether they match 'admin' '1234'

def match(user_name,pswd):
    match_usercheck = user_name == "admin"
    match_pswdcheck = pswd == "1234"
    both_match = match_usercheck and  match_pswdcheck
    print ("Entered details has been matched :")

get_userdetails = input("Enter user name : ")
get_pswddetails = input("Enter password details: ")
match_check = match(get_userdetails,get_pswddetails)


def check_num(number):
    postive_num = number > 0
    print("Entered number is postive: ",postive_num)  
    negative_num = number < 0
    print("Entered number is negative: ",negative_num)
    equal_num = number == 0
    print("Entered number is equal to zero: ",equal_num)
    even_num = number % 2 == 0
    print("Entered number is even: ",even_num)
    print("Entered number is odd: ", not even_num)

number = int(input("Enter a number: "))
check_num(number)
