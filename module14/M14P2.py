class Student:
    def __init__(self, first, last, code, credits):
        self.first = first
        self.last = last
        self.code = code
        self.credits = credits
    def tuition(self):
        if self.code == "I":
            cost = 250
        else:
            cost = 500
        total = self.credits*cost
        return total
student1 = Student("Mary", "Johnson", "I", 12)
student2 = Student("David", "Brown", "O", 9)

print("student information")
print(student1.first, student1.last)
print("District Code:", student1.code)
print("Credits:", student1.credits)
print("Tuition: $",student1.tuition())
print()

print("student information")
print(student2.first,student2.last)
print("District Code:", student2.code)
print("Credits:", student2.credits)
print("Tuition: $", student2.tuition())
