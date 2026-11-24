class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def bonus(self, rate):
        return self.salary*rate

emp1 = Employee("John Smith", 50000)

rate = .10

print("Employee:", emp1.name)
print("Salary: $", emp1.salary)
emp_bonus =emp1.bonus(rate)
print("Bonus rate:", rate)
print("Bonus amount: $", emp_bonus)
