# #checking a condition to print output
# marks=int(input("enter marks: ")) 
# if (marks>=80):
#      print("A")
# elif (marks>=60):
#      print("B")
# elif (marks>=40):
#      print("C")
# else:
#      print("fail")

# #checking more than conditions to print output 
# average_marks=int(input("enter marks: ")) #taking in the user's input as an int 
# if average_marks  >= 70:
#  		 print("A")
# elif average_marks  >= 60 and average_marks  < 70:
#  	     print("B")
# elif average_marks  >= 50 and average_marks  < 60:
#    		 print("C")
# elif average_marks  >= 40 and average_marks  < 50:
#    		 print("D")
# else:
#          print("E")

# #class task - classifying odd and even numbers
# number=int(input("type a number: "))
# if (number % 2 == 0):
#     print("even")
# else:
#     print("odd")

# #task to display the greatest number
# num1=int(input("number 1: "))
# num2=int(input("number 2: "))
# num3=int(input("number 3: "))

# if (num1 > num2) and num1 > num3:
#      print(num1,"is the largest")
# elif (num2 > num1) and num2 > num3:
#      print(num2,"is the largest")
# else:
#      print(num3,"is the largest")

#no 2
temp = float(input("enter temperature: "))
if (temp > 30.0) and temp < 100.0 :
     print("the temperature is too high")
elif (temp <= 30.0) and temp > 15.5:
     print("normal temperature")
elif (temp > 100.0):
     print("extreme temperature")
else:
     print("normal temperature")

