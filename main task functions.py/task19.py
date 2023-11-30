#Continue with the same program and find the person's
#  PAYEE using the taxable income above.
#Find the Kenya PAYEE Tax Rate using THIS LINK
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

#calc NSSF
def calc_nssf(gross_salary, rate = 0.06):   
    if (gross_salary < 18000) and (gross_salary > 0):
        nssf = rate*gross_salary
    else:
        nssf = 18000*rate
    return nssf

tnssf = calc_nssf(gross_salary)
print(f"NSSF {tnssf}")

#calc NHDF
def calc_nhdf(gross_salary, rate = 0.015):
    nhdf = gross_salary*rate
    return nhdf

tnhdf = calc_nhdf(gross_salary)
print(f"NHDF {tnhdf}")

#taxable income
def calc_tax(gross_salary,tnssf,tnhdf):
    taxable_income = gross_salary - (tnssf + tnhdf)
    return taxable_income

ttax_income = calc_tax(gross_salary,tnssf,tnhdf)
print(f"taxable income {ttax_income}")

#PAYEE
def calc_payee(ttax_income):
    if (ttax_income > 0) and (ttax_income <= 24000):
        payee = (0.1*ttax_income) - 2400
    elif (ttax_income > 24000) and (ttax_income <= 32333):
        payee = (0.25*(ttax_income - 24000) + (0.1*24000))-2400
    else: 
        payee = (0.3*(ttax_income-32333) + (0.1*24000) + (0.25*8333))-2400
    return payee

tpayee = calc_payee(ttax_income)
print(f"PAYEE {tpayee}")

