#Write a program that takes input of 2 values and 
# adds them. The program should only accept numbers 
# and floats only or otherwise display an error 
# “invalid character entered” and take the user 
# to re-enter the inputs .
d1 = (input("enter number: "))
d2 = (input("enter number: "))
d3 = d1 + d2
if (type(d1)!= "float") and (type(d2)!= "float"):
    print("invalid character entered")
else:
    print(d3)