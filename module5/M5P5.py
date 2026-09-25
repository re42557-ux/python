last_name =input("Last name: ")
dependents =int(input("Number of dependents: "))
gross_income =float(input("Gross income: "))

adjusted_income =gross_income-(dependents * 12000)
if adjusted_income > 50000:
    tax_rate = .20
else:
    tax_rate = .10
income_tax =adjusted_income*tax_rate
if income_tax < 0:
    income_tax = 100
print("Last Name:", last_name)
print("Gross Income:", gross_income)
print("Dependents:", dependents)
print("Adjusted Gross Income:", adjusted_income)
print("Income Tax:", income_tax)
