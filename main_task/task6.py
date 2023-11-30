#Write a program input a password. Give them only 4
#  attempts to check the passwords entered against 
# “admin@123”. If the password is correct access is
#  granted. After you show them a message ,
#  the account is blocked.

password = input("enter password: ")
correct_pass = "admin@123"
attempts = 4
for i in range(attempts):
    if (password == correct_pass):
        print("access granted")
        break
    else:
        print("incorrect password")
        attempts+=1
        if attempts==4:
            print("account blocked")

#research on loops