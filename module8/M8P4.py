total_sales = 0.0
order_count = 0

print(f"{'item':<12}{'quantity':>10}{'price':>12}"
      f"{'extended':>14}")
print("-" * 48)

with open("M8P4Orders.txt", "r") as infile:
    lines =infile.readlines()
for i in range(0, len(lines), 3):
    item =lines[i].strip()
    quantity =int(lines[i +1].strip())
    price =float(lines[i +2].strip())

    extended_price =quantity*price
    total_sales += extended_price
    order_count += 1
    print(f"{item:<12}{quantity:>10}"
          f"${price:>11,.2f}${extended_price:>13,.2f}")

if order_count > 0:
    average_order = total_sales/order_count
else:
    average_order = 0.0
print("-" * 48)
print(f"total extended prices: ${total_sales:,.2f}")
print(f"Number of orders: {order_count}")
print(f"Average order: ${average_order:,.2f}")
