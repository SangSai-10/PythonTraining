
def tax_rate(income):
    if (income >= 4000 and income <8000):
        print("Income",income," fall under Indian tax rate : 5%")
    if (income >= 8000 and income <12000): 
        print("Income",income," fall under Indian tax rate : 10%")
    if (income >= 12000 and income <16000): 
        print("Income",income," fall under Indian tax rate : 15%")
    if (income >= 16000 and income <20000): 
        print("Income",income," fall under Indian tax rate : 20%")
    if (income >= 20000 and income <24000): 
        print("Income",income," fall under Indian tax rate : 25%")
    if (income>= 24000):
        print("Income",income," fall under Indian tax rate : 30%")    

annual_income = int(input("Enter user annual income:"))
tax_rate(annual_income)
 
def metal(metal_name):
    if metal_name == "Gold":
        print("The price of Gold rate is 1800")
    if metal_name == "Silver":
        print("The price of Silver rate is 1000")
    if metal_name == "Platinum":
        print("The price of Platinum rate is 5000")
                
metal_name = input("Enter the metal name: ")
metal(metal_name)

def number(num):
    if num % 2 == 0 :
        print("The number is even",num)
        return num
    else:
        num = num * 2
        print("The number is odd:",num)
        return num
    
get_number = int(input("Enter the number: "))
odd_even = number(get_number)


def max_mincheck(number1,number2):
    if number1 > number2 :
        print("The given number is maximum than other number",number1)
    if number2 > number1 :
        print("The given number is maximun than other number", number2)
    if number1 == number2:
        print("The given both number are equal")

max_mincheck(40,60)   

def max_mincheck(number1,number2):
    if number1 < number2 :
        print("The given number is minimum than other number",number1)
    if number2 < number1 :
        print("The given number is minimum than other number", number2)
    if number1 == number2:
        print("The given both number are equal")

max_mincheck(40,60)   


def weekcalendar(day):
    if day == 1 :
        print("The day is Monday")
    if day == 2 :
        print("The day is Tuesday")
    if day == 3 :
        print("The day is Wednesday")
    if day == 4 :
        print("The day is Thursday")
    if day == 5 :
        print("The day is Friday")
    if day == 6 :
        print("The day is Saturday")
    if day == 7 :
        print("The day is Saturday")

get_day = int(input("Enter the day:"))
weekcalendar(get_day)


def student_score(marks):
    pass_fail = marks >= 36
    return pass_fail

marks = 40
exam_result = student_score(marks)
if exam_result == True :
    print("The student passed the exam")
else:
    print("The studen failed the exam")

def roomtemp(temp):
    if temp >= 21 and temp <= 24:
        print("The temparature is normal", temp)
    if temp > 24:
        print("The temparature is hot", temp)
    if temp <21 :
        print("The temparature is cold", temp)
    
    
temperature = 21
roomtemp(temperature)
