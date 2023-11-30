weekdays=["monday","tuesday","wednesday","thursday","friday"]
print(weekdays[-3])

#using the index fuction to find the index of a var in a list
weekdays=["monday","tuesday","wednesday","thursday","friday"]
print(weekdays.index("wednesday"))

trainees = ["John", [2, ["James","Mary"]]]
print(trainees[1][-2]) #to access no 2 from list within a list 
print(len(trainees))

add_list=trainees+weekdays #concatenate method
print(add_list)

add_list=trainees+weekdays #membership
#print(add_list)
print("John" in add_list) # in/not in are membership operators
#👆🏾 will output a boolean to confirm membership of the var in that list

#updating a list
weekends=["saturday","tuesday"]
weekends[1]="sunday"
print(weekends)

#to add values to a list use the append function
weekends=["saturday","tuesday"]
weekends.append("holidays")
print(weekends)

#deleting a list
weekends=["saturday","tuesday"]
del(weekends[-1])
print(weekends)

numbers=[1,2,3,4,5]
#numbers.pop(-3) #.pop function removes the specific index
numbers.insert(0,"digits")
print(numbers)

#try the list functions => .clear, .reverse, .extend, .count, .pop
numbers=[1,2,3,4,5]
numbers.clear()
print(numbers)

numbers=[1,2,3,4,5]
numbers.reverse()
print(numbers)

numbers=[1,2,3,4,5]
numbers.count(0)
print(numbers)

#task:lists
trainees = ["John", [2, ["James","Mary"]]]
print(trainees[1][0])

print(trainees[1][1][0])

trainees.append(56)
print(trainees)

trainees.insert(0,"Mike")
print(trainees)

# trainees = ["John", [2, ["James","Mary"]]]
# trainees[1][1].remove("Mary")

trainees = ["John", [2, ["James","Mary"]]]
trainees[1][1].insert(1,56)
print(trainees)

trainees = ["John", [2, ["James","Mary"]]]
trainees[1][0]=8
print(trainees)



