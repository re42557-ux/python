def print_players(players):
    print("baseball player batting averages")
    print("-----------------------------")
    print("player name       batting average")

    for name in players:
        print(name, "             ", players[name])

players = {}
try:
    file = open("M13P3players.txt", "r")

    for line in file:
        data = line.strip().split(",")
        name = data[0]
        average = float(data[1])
        players[name] = average

    file.close()

    print_players(players)
except FileNotFoundError:
    print("could not find M13P3players.txt")
