answer = input("do you want to enter an order? yes or no: ")
total_discount = 0
while answer.lower() == "yes":
    quantity = int(input("enter quantity: "))
    price = float(input("enter price per item: "))
    extended = quantity * price
  
    if extended > 10000:
        discount =extended*.25
    else:
        discount = extended*.10

    total = extended-discount
    print("extended price:$", round(extended, 2))
    print("discount amount: $", round(discount, 2))
    print("order total:$", round(total, 2))

    total_discount =total_discount+discount

    answer = input("do you want to enter another order? yes or no: ")
print("total discounts: $",round(total_discount, 2))
