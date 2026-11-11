# problem 5
# search for a player and display a message if not found
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
    print("player names and batting averages")
    for i in range(len(names)):
        print(names[i], averages[i])

def search_player(search_name):
    found = False
    for i in range(len(names)):
        if names[i] == search_name:
            print(names[i], averages[i])
            found = True
    if found == False:
        print("name not found")
# Main program
load_data()
display_players()
answer = ""
while answer != "QUIT":
    answer = input("\nenter a player's last name or QUIT: ")
    if answer != "QUIT":
        search_player(answer)
