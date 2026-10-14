total_tuition = 0.0
student_count = 0

print(f"{'student':<12}{'credits':>10}{'Tuition':>14}")
print("-" * 36)

with open("M8P5Students.txt", "r") as infile:
    lines = infile.readlines()
for i in range(0, len(lines), 3):
    last_name =lines[i].strip()
    district_code =lines[i + 1].strip().upper()
    credits =int(lines[i + 2].strip())
    if district_code == "I":
        cost_per_credit = 250.00
    else:
        cost_per_credit = 500.00

    tuition =credits*cost_per_credit
    total_tuition += tuition
    student_count += 1
    print(f"{last_name:<12}{credits:>10}"
          f"${tuition:>13,.2f}")
print("-" * 36)
print(f"total tuition owed: ${total_tuition:,.2f}")
print(f"number of students: {student_count}")
