start = int(input("enter start value: "))
stop = int(input("enter stop value: "))
increment = int(input("enter increment value: "))

number = start
if increment == 0:
    print("increment cant be zero")
else:
    while (increment > 0 and number <= stop) or (increment < 0 and number >= stop):
        print(number)
        number =number + increment
