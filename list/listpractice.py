# # **********************************1****************************************************

# marks = [56, 54, 100, 35, 83, 81, 100, 66, 93, 81, 79, 67, 100, 50, 74, 59, 100, 61, 37, 60]

# def scored_centum(marks): 

#     centum_count = 0
#     for i in  marks:
#        if i == 100:
#         centum_count = centum_count + 1
#     return centum_count
        
# centum_total = scored_centum(marks)
# print("Students scored centum in math :",centum_total)
# # ********************************************2*****************************************
# def student_grade_count(marks): 

#     gradeA = 0
#     gradeB = 0
#     gradeC = 0
#     gradeD = 0
#     for i in  marks:
#        if i > 90:
#          gradeA = gradeA + 1
#        elif i > 80 and i < 90:
#          gradeB = gradeB + 1 
#        elif i > 60 and i < 80:
#          gradeC = gradeC + 1
#        else:
#           gradeD = gradeD + 1
#     return gradeA,gradeB,gradeC,gradeD

# marks = [56, 54, 100, 35, 83, 81, 100, 66, 93, 81, 79, 67, 100, 50, 74, 59, 100, 61, 37, 60]       
   
        
# gradeA,gradeB,gradeC,gradeD = student_grade_count(marks)
# print("Students scored in gradeA :",gradeA)
# print("Students scored in gradeB :",gradeB)
# print("Students scored in gradeC :",gradeC)
# print("Students scored in gradeD :",gradeD)

# # ********************************3************************************************************
# def student_grade_count(marks,grade): 

#     for i in  marks:
#        if i > 90:
#           grade.append("GradeA")
#        elif i > 80 and i < 90:
#           grade.append("GradeB")
#        elif i > 60 and i < 80:
#           grade.append("GradeC")
#        else:
#           grade.append("GradeD")
#     return grade

# marks = [56, 54, 100, 35, 83, 81, 100, 66, 93, 81, 79, 67, 100, 50, 74, 59, 100, 61, 37, 60] 
# grade =[]         
        
# result_grade = student_grade_count(marks,grade)
# print(result_grade)

# # **************************************4******************************************
# numbers = [6, 8, 10, 7, 9] 
# reverse =[]
# size = len(numbers)
# for i in range(0,size,1):
#      x= numbers.pop()
#     #  print(x)
#     #  reverse.insert(size-1,x)
#      reverse.append(x)
# print(reverse)

# # ***************************************5*******************************************
# numbers = [1, 2, 3, 4, 5]
# n = 2 
# for i in range(0,n,1): 
#     last = numbers.pop() 
#     numbers.insert(0, last) 
#     print(numbers)
# # ***************************************6********************************************
numbers = [1, 2, 3, 4, 5]
fact = 2
factlist = []
for i in numbers:
    fact = fact * i
    factlist.append(fact)
    
print(factlist)

   