# problem 4
# display players and search for a batting average
names = []
averages = []
def load_data():
    file = open("M12P4player.txt", "r")
    for line in file:
        data = line.strip().split(",")
        names.append(data[0])
        averages.append(float(data[1]))
    file.close()
  
def display_players():
    print("Player Names and Batting Averages")
    for i in range(len(names)):
        print(names[i], averages[i])
      
def search_player(search_name):
    for i in range(len(names)):
        if names[i] == search_name:
            print(names[i], averages[i])
# Main program
load_data()
display_players()
answer = ""
while answer != "QUIT":
    answer = input("\nenter a player's last name or QUIT: ")

    if answer != "QUIT":
        search_player(answer)
