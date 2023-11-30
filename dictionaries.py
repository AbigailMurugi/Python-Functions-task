#creating dictionaries
# person = {
#     "name":"Jameel",
#     "age":27,
#     "location":"Niamey",
#     "email":"jameel@gmail.com"
# }
#accessing values in a dictionary - use keys
# print(person["age"])
# print(person["email"])

# #changing a value in a dictionary
# person["age"]=20
# print(person)

# person["location"]="Dakar"
# print(person)

# person["email"]="j.meel23@gmail.com"
# print(person)

# #adding a new key value pair 
# person["gender"]="Male"
# print(person)

# person["status"]="single"
# print(person)

#person["id"]=2323,["nationality"]="sudanese"

#introduce more than one key value pair
person = {"name":"Jameel","age":27,"location":"Niamey","email":"jameel@gmail.com"}
new_data={"address":2343,"status":"single"}
person.update(new_data)
print(person)

#dictionary functions 
print(person.get("age")) #returns what is defined in the parenthesis
print(person.pop("name")) #used to display what has been removed from the dictionary
print(person.keys()) #displays the keys 
print(person.values()) #displays the values
print(person.popitem()) #removes the last function
print(len(person)) #function to get the length of the dictionary



