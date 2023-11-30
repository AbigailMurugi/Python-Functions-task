#Write a program that prints the largest of 4 inputs
#  taken in from a user. Assume that the user would 
#  enter any two numbers which are the same
d1 = int(input("enter no: "))
d2 = int(input("enter no: "))
d3 = int(input("enter no: "))
d4 = int(input("enter no: "))

if (d1>=d2) and (d1>=d3) and (d1>=d4):
    print(d1,"is the largest")
elif (d2>=d1) and (d2>=d3) and (d2>=d4):
    print(d2, "is the largest")
elif (d3>=d1) and (d3>=d2) and (d3>=d4):
    print(d3, "is the largest")
else:
    print(d4,"is the largest")