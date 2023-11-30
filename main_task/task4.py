#Write a program which accepts email as form input or
# from terminal. Validate the email by checking if 
# it's a valid email. 
email = str(input("enter email:  "))
if "@" in email and "." in email:
    print("valid email")
else:
    print("invalid email")

#research on 