def getForecast(month, sales):
    month = month.lower()
    if month in ["jan", "feb", "mar"]:
        percent =0.10
    elif month in ["apr", "may", "jun"]:
        percent =0.15
    elif month in ["jul", "aug", "sep"]:
        percent =0.20
    else:
        percent =0.25

    nextSales= sales*(1 + percent)
    return nextSales
  
answer = "yes"

while answer == "yes":
    lastName = input("enter last name: ")
    month = input("enter month (Jan, Feb, etc.): ")
    sales = float(input("enter sales: $"))

    forecast = getForecast(month, sales)

    print(lastName, "next month's forecast is $", round(forecast, 2))

    answer =input("do you want to continue? (yes or no): ").lower()
