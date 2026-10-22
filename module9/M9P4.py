def getRate(code):
    if code == "L":
        return 25
    elif code == "A":
        return 30
    elif code == "J":
        return 50
    else:
        return 0
totalPay = 0
again = "Y"
while again =="Y":
    name = input("Enter last name: ")
    code = input("Enter job code (L, A, J): ").upper()
    hours = float(input("Enter hours worked: "))
    rate = getRate(code)
    if hours >40:
        pay = (40 * rate)+((hours-40)*rate * 1.5)
    else:
        pay = hours*rate
    print("Name:", name)
    print("Gross pay:", round(pay, 2))
    totalPay =totalPay + pay

    again = input("Another employee? Y or N: ").upper()

print("Total gross pay:", round(totalPay, 2))
