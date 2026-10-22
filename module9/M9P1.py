def getTotal(qty, price):
    total = qty * price
    if total > 10000:
        total = total * .90
    return total
grandTotal = 0
again = "Y"
while again == "Y":
    qty = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    total = getTotal(qty, price)

    print("Quantity:", qty)
    print("Price:", price)
    print("Extended price:", total)
    grandTotal = grandTotal + total

    again = input("Another item? Y or N: ").upper()
print("Total extended price:", grandTotal)
