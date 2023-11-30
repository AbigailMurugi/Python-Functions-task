#Write a program called stars. It should prompt the 
# user for a number, and it should print the number
#  of stars till the number entered.
# Example If rows is 5, it should print the following:
# *
# **
# ***
# ****
stars = "*"
count = 0
number = int(input("number:" ))
for i in range(number):
    stars+="*"
    count+=1 
    print(stars)