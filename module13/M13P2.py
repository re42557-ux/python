students = {
    "John": [85, 90, 88],
    "Mary": [92, 95, 90],
    "James": [78, 82, 80],
    "Sarah": [95, 98, 96],
    "David": [88, 85, 90]
}

def get_averages(students):
    averages = []
    for name in students:
        grades = students[name]
        average = sum(grades) / 3
        averages.append([name, average])
    return averages

averages = get_averages(students)
print("student grade averages")
print("-----------------------------")
print("student name       average")
for student in averages:
    print(student[0], "          ", round(student[1], 2))

grade1 = 0
grade2 = 0
grade3 = 0
for name in students:
    grade1 = grade1 + students[name][0]
    grade2 = grade2 + students[name][1]
    grade3 = grade3 + students[name][2]

grade1 = grade1/len(students)
grade2 = grade2/len(students)
grade3 = grade3/len(students)

print("-----------------------------")
print("Class Grade Averages")
print("Grade 1 Average:", round(grade1, 2))
print("Grade 2 Average:", round(grade2, 2))
print("Grade 3 Average:", round(grade3, 2))
