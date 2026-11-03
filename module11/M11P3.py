def commission(sales):
    if sales > 100000:
        comm = sales*.10
    else:
        comm = sales*.05
    target = sales*.05
    return comm, target

name = input("enter salesperson last name: ")
sales = float(input("enter sales amount: "))

comm, target =commission(sales)
print("salesperson:", name)
print("commission:", comm)
print("next year's target:", target)
