name =input("Name of the appliance: ")
cost =float(input("Cost of the appliance: "))

if cost > 1000:
    warranty = cost * .10
else:
    warranty = cost * .05

total=cost+warranty
print("Name:", name)
print("Cost:", cost)
print("Warranty:", warranty)
print("Total:", total)
