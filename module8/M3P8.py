total_bonus = 0.0
print(f"{'employee':<12}{'salary':>12}{'bonus':>12}")
print("-" * 36)
with open("M8P3Employees.txt", "r") as infile:
    lines = infile.readlines()

for i in range(0, len(lines), 2):
    last_name = lines[i].strip()
    salary = float(lines[i + 1].strip())

    if salary >= 100000:
        rate = 0.20
    elif salary >= 50000:
        rate = 0.15
    else:
        rate = 0.10
    bonus =salary*rate
    total_bonus += bonus
    print(f"{last_name:<12}${salary:>11,.2f}"
          f"${bonus:>11,.2f}")

print("-" * 36)
print(f"Total bonuses paid: ${total_bonus:,.2f}")
