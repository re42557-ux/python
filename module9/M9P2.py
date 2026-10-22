def getAverage(hits, atBats):
    if atBats == 0:
        return 0
    return hits / atBats
count = 0
again = "Y"
while again == "Y":
    name = input("Enter last name: ")
    hits = int(input("Enter hits: "))
    atBats = int(input("Enter at bats: "))
    avg = getAverage(hits, atBats)

    print("Name:", name)
    print("Batting average:", round(avg, 3))
    count = count + 1
    again = input("Another player? Y or N: ").upper()

print("Players entered:", count)
