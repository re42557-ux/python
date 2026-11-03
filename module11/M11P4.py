def bowling(score1, score2, score3):
    average = (score1+score2+score3) / 3
    basis = 200
    percentage = .90

    handicap = (basis-average)*percentage
    if handicap < 0:
        handicap = 0
    average_handicap = average+handicap

    return average, average_handicap

name = input("enter bowler's last name: ")

game1 = float(input("enter first game score: "))
game2 = float(input("enter second game score: "))
game3 = float(input("enter third game score: "))

avg, avg_handicap = bowling(game1, game2, game3)

print("bowler:", name)
print("average score:", avg)
print("average score with handicap:", avg_handicap)
