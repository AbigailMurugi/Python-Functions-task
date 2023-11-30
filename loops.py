# # n="10"
# # for i in n:
# #     print(i)

# # # for i in range(0,1000):
# # #     print(i)

# #looping through a list
# nov_intake=["anthony","tosh","ramadhan","cornelius",
# "lilian","herman","bilal","iano","abigail"]

# for i in nov_intake:
#     if i==nov_intake[5]:#breaks at the number before the indicated one
#         break
#     print(i)


# #looping through control statements (if statements)
# for i in range (20):
#     if (i==5):
#         continue #used to skip the rest of the code in a loop
#     print(i)

# #looping through control statements (if statements)
# for i in range (20):
#     if (i==5):
#         break #used to stop a loop prematurely
#     print(i)

# #looping through dictionaries 
# person = {
#     "name":"Jameel",
#     "age":27,
#     "location":"Niamey",
#     "email":"jameel@gmail.com"
# }
# for key,value in person.items():
#     print(key,value)

#do task on slide 56
#display 1-50 in a list
# number=[]
# for i in range(1,51):
#     number.append(i)
# print(number)

# digits=[]
# for i in range(1,51):
#     if (i % 7 == 0) or (i % 5 == 0):
#         digits.append(i)
# print(digits)
# #print(f"{digits}digits") this is allows us to pass a variable inside a string 

# #find sum range between 10-40
# values=[]
# for i in range(10,41):
#     values.append(i)
# sumation = sum(values)
# average = sumation/len(values)
# print(f"{sumation} sum")
# print(f"{average} average")

#list odd numbers between 10-50
main=[]
for i in range(10,50):
    if i % 2 != 0:
        main.append(i)
        if len(main)==10:
            break
print(f"{main} main")
       