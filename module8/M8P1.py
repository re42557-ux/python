principal = float(input("enter principal amount: "))
rate = float(input("enter interest rate: "))
total = 0
print("year  beginning balance  ending balance")

for year in range(1, 6):
    beginning =principal
    interest =beginning*rate
    ending =beginning+interest

    print(year, "$" + format(beginning, ",.2f"),
          "$" + format(ending, ",.2f"))
    total = total+interest
    principal = ending

print("total interest earned: $",format(total, ",.2f"))
