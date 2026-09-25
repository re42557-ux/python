item = input("Item: ")
quantity = int(input("Quantity: "))
if item == "A":
    unit_price =10.00
else:
    unit_price =20.00
extended_price =quantity * unit_price

print("Item:", item)
print("Unit Price: $",format(unit_price, ".2f"))
print("Extended Price: $",format(extended_price, ".2f"))
