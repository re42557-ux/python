def getTicketPrice(miles):
    if miles >= 30:
        price = 12
    elif miles >= 20:
        price = 10
    elif miles >= 10:
        price = 8
    else:
        price = 5
    return price

answer ="yes"
totalTickets = 0

while answer == "yes":
    lastName = input("enter last name: ")
    miles = float(input("enter miles from downtown Chicago: "))
    price = getTicketPrice(miles)
    print(lastName, "ticket price: $", price)
    totalTickets = totalTickets + price
    answer = input("do you want to continue? (yes or no): ").lower()

print("total price of all tickets: $", totalTickets)
