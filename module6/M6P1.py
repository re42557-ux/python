quantity =int(input("Enter quantity of widgets: "))

if quantity > 10000:
    price = 10
elif quantity >= 5000:
    price = 20
else:
    price = 30
extended =quantity*price
tax =extended*.07
total =extended+tax
print()
print("Extended Price:$", format(extended, ",.2f"))
print("Tax:$", format(tax, ",.2f"))
print("Total:$", format(total, ",.2f"))
