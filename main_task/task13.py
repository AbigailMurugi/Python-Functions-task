#Write a program that takes the email and password 
# as input from a user and checks if they are equal
#  to “admin@mail.com” and password is “Admin@123” , 
# if so then print  “Login is Successful” and if not
#  print “Invalid username or password”. ONLY accept
#  3 tries after which it notifies you that you have 
# been blocked.
email = input("enter email: ")
password = input("password: ")

c_email = "admin@mail.com"
c_pass = "Admin@123"
attempts = 3

for i in range(attempts):
    if (email == c_email) and (password == c_pass):
        print("Login is Successful")
        break
    print(" ")
    elif (i in range(attempts)):
        print("")