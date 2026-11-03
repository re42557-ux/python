total = 0
tax = 0
def calculate(qty, price):
    global total
    global tax
    total = qty*price
    tax = total*.07
  
qty = int(input("enter quantity: "))
price = float(input("enter unit price: "))
calculate(qty, price)
print("total:", total)
print("tax:", tax)
