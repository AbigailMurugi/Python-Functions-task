# my_ds=[23, "Jane", (560), ["lesson", "maths", 
# {"currency" : "kes"}], 987, (76,"john")]

# #print kes
# print(my_ds[3][2]["currency"])

# #print 560
# print(my_ds[2])

# #print maths 
# print(my_ds[3][1])

# #add another key amount  with value 90
# my_ds[3][2]["amount"]=90
# print(my_ds)

# #reverse 987 to 789
# my_ds[4]=str(my_ds[4])
# 987
# #print(my_ds)
# print(my_ds[4][2::-1]) #practice strings

# # change John to Jane
# my_ds[5] = list(my_ds[5])
# my_ds[5][1] = "Jane"
# my_ds[5] = tuple(my_ds[5])
# print(my_ds)

my_ds = [23, "Jane", (560), ["Lesson", "Maths",
 {"currency" : "KES"}], 987, (76,"John")]

print(my_ds[3][2]["currency"])

print(my_ds[2])

print(my_ds[3][1])

my_ds[3][2]["account"]=20
print(my_ds)

my_ds[-1]=list(my_ds[-1])
my_ds[-1][1]="jane"
my_ds[-1]=tuple(my_ds[-1])
print(my_ds[-1])
