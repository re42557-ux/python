def getMPG(miles, gallons):
    if gallons == 0:
        return 0
    return miles / gallons
  
count = 0
again = "Y"

while again == "Y":
    city = input("Enter destination city: ")
    miles = float(input("Enter miles traveled: "))
    gallons = float(input("Enter gallons used: "))
    mpg = getMPG(miles, gallons)
    print("City:", city)
    print("Miles:", miles)
    print("MPG:", round(mpg, 2))

    count = count + 1
    again = input("Another trip? Y or N: ").upper()
print("Number of trips:", count)
