students = {
    "John": 85,
    "Mary": 92,
    "James": 78,
    "Sarah": 95,
    "David": 88
}
total = 0
print("student grades")
print("-----------------------------")
print("student name     grade")
for name in students:
    print(name, "          ", students[name])
    total = total+students[name]
average = total/len(students)

print("-----------------------------")
print("class average:", round(average, 2))
