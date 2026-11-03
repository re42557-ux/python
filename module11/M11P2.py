def scores(score1, score2, score3):
    total = score1+score2+score3
    average = total/3
    return total, average
name = input("enter student's last name: ")

exam1 = float(input("enter first exam score: "))
exam2 = float(input("enter second exam score: "))
exam3 = float(input("enter third exam score: "))

total, average = scores(exam1, exam2, exam3)

print("student:", name)
print("total points:", total)
print("average score:", average)
