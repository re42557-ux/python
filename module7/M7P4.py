answer = input("do you want to enter employee data? yes or no: ")
total = 0
count = 0
while answer.lower() == "yes":
    name = input("enter employee last name: ")
    hours = float(input("enter hours worked: "))
    rate = float(input("enter hourly pay rate: "))
    if hours <= 40:
        pay = hours*rate
    else:
        pay = (40 * rate) + ((hours - 40) * rate * 1.5)
    print("employee:", name)
    print("gross pay:$", round(pay, 2))
    total =total + pay
    count =count + 1
    answer = input("do you want to enter another employee? yes or no: ")

print("total gross pay: $", round(total, 2))
print("number of employees:", count)
if count > 0:
    average =total/count
    print("average pay:$", round(average, 2))
else:
    print("average pay: $0.00")
