item =input("part number: ")
quantity =int(input("quantity: "))

if item == "10" or item == "55":
    cost = 1.00
elif item == "99":
    cost = 2.00
elif item == "80" or item == "70":
    cost = 3.00
else:
    cost = 5.00
total = quantity*cost
print()
print("part Number:", item)
print("cost Per Unit: $",format(cost, ".2f"))
print("total Cost:  $", format(total, ".2f"))
