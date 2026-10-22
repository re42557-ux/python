def getTuition(hours, code):
    if code == "I":
        return hours * 250
    elif code == "O":
        return hours * 550
    else:
        return 0
total = 0
again = "Y"
while again == "Y":
    name = input("Enter student last name: ")
    hours = int(input("Enter credit hours: "))
    code = input("Enter district code (I or O): ").upper()
    tuition = getTuition(hours, code)

    print("Student:", name)
    print("Tuition owed:", tuition)

    total =total +tuition
    again =input("Another student? Y or N: ").upper()
print("Total tuition:", total)
