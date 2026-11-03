def discount(quantity, price, rate):
    amount = quantity*price*rate
    new_price = (quantity*price)- amount
    return amount, new_price
  
qty = int(input("enter quantity: "))
price = float(input("enter price: "))
rate = float(input("enter discount rate (example .10): "))

disc, final_price = discount(qty, price, rate)

print("quantity:", qty)
print("price:", price)
print("discount amount:", disc)
print("discounted price:", final_price)
