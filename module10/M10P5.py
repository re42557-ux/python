def getAssessedValue(county, marketValue):
    county = county.lower()
    if county == "cook":
        percent =0.90
    elif county == "dupage":
        percent =0.80
    elif county == "mchenry":
        percent =0.75
    elif county == "kane":
        percent =0.60
    else:
        percent =0.70
    assessedValue = marketValue*percent
    return assessedValue

answer = "yes"
totalMarket = 0
totalAssessed = 0

while answer == "yes":
    county = input("enter county: ")
    marketValue = float(input("enter home market value: $"))
    assessed = getAssessedValue(county, marketValue)
    print("assessed value: $", round(assessed, 2))
    totalMarket = totalMarket + marketValue
    totalAssessed = totalAssessed + assessed
    answer = input("do you want to continue? (yes or no): ").lower()
print("total market values: $", round(totalMarket, 2))
print("total assessed values: $", round(totalAssessed, 2))
