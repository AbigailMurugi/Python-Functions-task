#Write a program which gets a phone number from a form
# input or terminal. Validates the phone number by 
# checking if it starts with +254.. or 07.. or 71… 
# or 254.. or 01... Convert the number to start with 
# +254… 

cell = input("enter phone number: ")
# +254748023765
if (cell[0:4] == +254) and (len(cell) == 13):
    print(cell)
# 0748023767
elif (cell[0:2] == "07") and len(cell) == 10:
    new_cell = "+254" + cell[1:]
    print(new_cell)
#0148023767
elif  (cell[0:2] == "01") and len(cell) == 10:
     n_cell = "+254" + cell[1:]
     print(n_cell) 
#123456789
elif ((cell[0:1] == "1" and len(cell) == 9) or 
     (cell[0:1] == "7" and len(cell) == 9)): 
    cell1 = "+254" + cell
    print(cell1)
#254748023765
elif (cell[0:3] == "254") and (len(cell) == 12):
    cell2 = "+" + cell
    print(cell2)
else:
    print ("enter valid number")

