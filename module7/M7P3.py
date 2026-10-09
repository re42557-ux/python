answer = input("do you want to enter student data? yes or no: ")
count = 0
while answer.lower() == "yes":
    name = input("enter last name: ")
    score1 = float(input("enter first exam score: "))
    score2 = float(input("enter second exam score: "))

    average =(score1 + score2)/2

    print("last name:", name)
    print("average score:", average)
    count = count + 1
    answer = input("do you want to enter another student? yes or no: ")
print("number of students:", count)
