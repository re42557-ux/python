class Student:
    def __init__(self, first, last, code, credits):
        self.first =first
        self.last =last
        self.code =code
        self.credits =credits
    def tuition(self):
        rates = {
            "I":250,
            "O": 500,
            "X": 800,
            "G": 250
        }
        cost =rates[self.code]
        total = self.credits*cost
        return total
student1 = Student("Mary", "Johnson", "I", 12)
student2 = Student("David", "Brown", "O", 9)
student3 = Student("Sarah", "Williams", "X", 15)
student4 = Student("James", "Davis", "G", 12)
students = [student1, student2, student3, student4]
for s in students:
    print("Student:", s.first, s.last)
    print("District Code:", s.code)
    print("Credits:", s.credits)
    print("Tuition: $", s.tuition())
    print("-------------------")
