#Continue with the program above, then use  the gross
# salary to find the NSSF. 
#To find the Kenya NSSF Rate using. 
# Compute NSSF using 6% of the Gross Salary.
# BUT ONLY A MAXIMUM OF 18,000 CAN BE USED IN NSSF. 

salary = int(input("enter salary: "))
benefits = int(input("enter benefits: "))

#function to calculate gross salary
def calc_gross(a,b):
    gross = salary + benefits
    return gross

gross_salary = calc_gross(salary,benefits)
print(f"Gross salary {gross_salary}")

#function to calc NHIF using gross salary
def calc_nhif(gross_salary):
    if(gross_salary<=5999):
        nhif = 150
    elif (gross_salary>6000) and (gross_salary<=7999):
        nhif = 300
    elif (gross_salary > 8000) and (gross_salary <= 11999):
        nhif = 400
    elif (gross_salary > 12000) and (gross_salary <= 14999):
        nhif = 500
    elif (gross_salary > 15000) and (gross_salary <= 19999):
        nhif = 600
    elif (gross_salary > 20000) and (gross_salary <= 24999):
        nhif = 750
    elif (gross_salary > 25000) and (gross_salary <= 29999):
        nhif = 850
    elif (gross_salary > 30000) and (gross_salary <= 34999):
        nhif = 900
    elif (gross_salary > 35000) and (gross_salary <= 39999):
        nhif = 950
    elif (gross_salary > 40000) and (gross_salary <= 44999):
        nhif = 1000
    elif (gross_salary > 45000) and (gross_salary <= 49999):
        nhif = 1100
    elif (gross_salary > 50000) and (gross_salary <= 59999):
        nhif = 1200
    elif (gross_salary > 60000) and (gross_salary <= 69999):
        nhif = 1300
    elif (gross_salary > 70000) and (gross_salary <= 79999):
        nhif = 1400
    elif (gross_salary > 80000) and (gross_salary <= 89999):
        nhif = 1500
    elif (gross_salary > 90000) and (gross_salary <= 99999):
        nhif = 1600
    else:
        nhif = 1700
    return nhif

tnhif = calc_nhif(gross_salary)
print(f"NHIF {tnhif}")

def calc_nssf(gross_salary, rate = 0.06):   
    if (gross_salary < 18000) and (gross_salary > 0):
        nssf = rate*gross_salary
    else:
        nssf = 18000*rate
    return nssf

tnssf = calc_nssf(gross_salary)
print(f"NSSF {tnssf}")


