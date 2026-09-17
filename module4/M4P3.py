meal_total = float(input("total for the meal: "))

tip15 =meal_total * (0.15)
tip18 =meal_total * (0.18)
tip20 =meal_total * (0.20)

print("15% Tip:")
print(f"Total: {meal_total:.2f}")
print(f"Tip: {tip15:.2f}")
print(f"Total with Tip {meal_total + tip15:.2f}")

print("18% Tip:")
print(f"Total: {meal_total:.2f}")
print(f"Tip: {tip18:.2f}")
print(f"Total with Tip {meal_total + tip18:.2f}")

print("20% Tip:")
print(f"Total: {meal_total:.2f}")
print(f"Tip: {tip20:.2f}")
print(f"Total with Tip {meal_total + tip20:.2f}")
