purchase_price = float(input("price per share purchased: "))
current_price = float(input("current stock price: "))
quantity = float(input("quantity of stock: "))
value_change = (current_price - purchase_price) * quantity
print("Increase or decrease in stock value:",value_change)
