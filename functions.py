# #area of a triangle
# def area_triangle(a,b): #creates the function to get area 
#     area = (a*b)/2 #carries out the calculation 
#     return area

# base = float(input("enter base: "))
# height = float(input("enter height: "))

# triangle1 = area_triangle(base,height) #create a variable to call the function 
# print(triangle1)

# #create a function that checks for odd numbers 
# def check_numbers(a):
#     if (a % 2 == 0):
#         num = "even"
#     else: 
#         num = "odd"
#     return num

# number = int(input("enter number: "))
# nums = check_numbers(number)
# print(nums)

#task to get total, average and grade using function
def total_marks(math, eng, swa, sci, sos):
    total = math + eng + swa + sci + sos
    return total

a = int(input("enter math: "))
b = int(input("enter eng: "))
c = int(input("enter swa: "))
d = int(input("enter sci: "))
e = int(input("enter sos: "))

tmarks = total_marks(a,b,c,d,e)
print(f"total marks: {tmarks}")

def average_marks(tmarks):
    average = tmarks / 5
    return average

amarks = average_marks(tmarks)
print(f"average marks: {amarks}")

def grade(a):
    if (a > 79):
        score = "A"
    elif (a > 60) and (a <= 79):
        score = "B"
    elif (a > 59) and (a <= 69):
        score = "C"
    elif (a > 40) and (a <= 59):
        score = "D"
    elif(a < 40):
        score = "E"
    return score

grade_score = grade(amarks)
print(f"grade: {grade_score}")