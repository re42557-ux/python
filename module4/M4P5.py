fixed_costs = float(input("fixed costs: "))
price_per_unit = float(input("price per unit: "))
cost_per_unit = float(input("cost per unit: "))

break_even_point = fixed_costs / (price_per_unit - cost_per_unit)

print("Break even point:", break_even_point)
