def getCarPrice(MSRP, make, model, electricCode):
    make =make.lower()
    model =model.lower()
    electricCode =electricCode.upper()
    if electricCode == "Y":
        discount =0.30
    elif make == "honda" and model == "accord":
        discount =0.10
    elif make == "toyota" and model == "rav4":
        discount =0.15
    else:
        discount =0.05
    newPrice = MSRP*(1 - discount)
    finalPrice = newPrice*1.07
    return finalPrice

answer = "yes"
totalMSRP = 0
totalSales = 0

while answer == "yes":
    make = input("enter car make: ")
    model = input("enter car model: ")
    electricCode = input("is it electric? (Yes or No): ")
    MSRP = float(input("enter MSRP: $"))
    price = getCarPrice(MSRP, make, model, electricCode)
    print("out-the-door price: $", round(price, 2))
    totalMSRP = totalMSRP+MSRP
    totalSales = totalSales+price
    answer = input("do you want to continue? (Yes or No): ").lower()
print("Total MSRP: $", round(totalMSRP, 2))
print("Total sales price: $", round(totalSales, 2))
