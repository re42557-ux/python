num1 = 1
num2 = 1

for i in range(20):
    print(num1, end=" ")
    next_num = num1 + num2
    num1 = num2
    num2 = next_num
print()
