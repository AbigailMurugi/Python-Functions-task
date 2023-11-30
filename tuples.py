days=("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
print(days[-1])
print(len(days)) #prints the length of the tuple

days=list(days) #converts tuple into a list
days[3]="thur"
print(days)

days=tuple(days) #converts tuple into a list
print(days)
