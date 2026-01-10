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

def drive(age,license):
    result = age > 18 and license == False
    return result

age = 15 
license = False
eligible_to_drive  = drive(age,license)
print(" User eligible to drive:?" , eligible_to_drive)

age = 20
license = False
eligible_to_drive = drive(age,license)
print(" User eligible to drive:?" , eligible_to_drive)
print("_______________________________________________")

def student_score(marks):
    pass_fail = marks >= 35
    return pass_fail

marks = 40
exam_result = student_score(marks)
print("Student score pass mark:?", exam_result)
print("Student score fail mark:?", not exam_result)

def student_score(marks):
    pass_fail = marks < 34
    return pass_fail

marks = 25
exam_result = student_score(marks)
print("Student score pass mark:?",not exam_result)
print("Student score fail mark:?", exam_result)
print("_______________________________________________")

def can_vacinate(temp):
    fever = temp >= 100
    return fever

temp = 95
eligible_for_shot = can_vacinate(temp)
print("Eligible for shot:? ", not eligible_for_shot)



    