# problem 3
# find the highest and lowest exam scores
names = []
scores = []
def load_data():
    file = open("M12P3student.txt", "r")
    for line in file:
        data = line.strip().split(",")
        names.append(data[0])
        scores.append(int(data[1]))
    file.close()
  
def highest_score():
    high_var = 0
    high_index = 0
    for i in range(len(scores)):
        if scores[i] > high_var:
            high_var = scores[i]
            high_index = i
    print("\nhighest score:")
    print(names[high_index], high_var)
  
def lowest_score():
    low_var = 999
    low_index = 0
    for i in range(len(scores)):
        if scores[i] < low_var:
            low_var = scores[i]
            low_index = i
    print("\nlowest score:")
    print(names[low_index], low_var)

# main program
load_data()
highest_score()
lowest_score()
