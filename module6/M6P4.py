tickets =int(input("number of concert tickets: "))
if tickets >= 25:
    price = 50
elif tickets >= 10:
    price = 60
elif tickets >= 5:
    price = 70
else:
    price = 75
total = tickets*price
print()
print("Number of tickets:", tickets)
print("Price per ticket:$", format(price, ".2f"))
print("Total cost:$", format(total, ".2f"))
