last_name =input("employee last name: ")
salary =float(input("salary: "))
level =int(input("job level: "))
if level >= 10:
    bonus_rate= .25
elif level >= 5:
    bonus_rate= .20
else:
    bonus_rate= .10
bonus = salary * bonus_rate
print()
print("Employee Last Name:", last_name)
print("Bonus: $", format(bonus, ",.2f"))
