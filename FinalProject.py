# Car Spotting Database
cars = []
# Add a car
def add_car():
    print("\n--- Add a Car ---")
    make = input("Enter make: ")
    model = input("Enter model: ")
    year = input("Enter year: ")
    color = input("Enter color: ")
    location = input("Where did you see it? ")
    notes = input("Any extra notes? ")
    car = {
        "make": make,
        "model": model,
        "year": year,
        "color": color,
        "location": location,
        "notes": notes
    }
    cars.append(car)
    print("\nCar added successfully!")

# View all Cars
def view_cars():
    print("\n--- All Spotted Cars ---")
    if len(cars) == 0:
        print("No cars in the database.")
    else:
        for i in range(len(cars)):
            print("\nCar #", i + 1)
            print("Make:", cars[i]["make"])
            print("Model:", cars[i]["model"])
            print("Year:", cars[i]["year"])
            print("Color:", cars[i]["color"])
            print("Location:", cars[i]["location"])
            print("Notes:", cars[i]["notes"])
          
# Find a car
def find_car():
    print("\n--- Find a Car ---")
    search = input("Enter a make or model: ").lower()
    found = False
    for car in cars:
        if search in car["make"].lower() or search in car["model"].lower():
            print("\nCar Found!")
            print("Make:", car["make"])
            print("Model:", car["model"])
            print("Year:", car["year"])
            print("Color:", car["color"])
            print("Location:", car["location"])
            print("Notes:", car["notes"])
            found = True
    if found == False:
        print("Car not found.")
      
# Delete a car
def delete_car():
    print("\n--- Delete a Car ---")
    view_cars()
    if len(cars) > 0:
        number = int(input("\nEnter car number to delete: "))
        if number > 0 and number <= len(cars):
            cars.pop(number - 1)
            print("Car deleted!")
        else:
            print("Invalid car number.")

# Save cars to a text file
def save_cars():
    file = open("cars.txt", "w")
    for car in cars:
        file.write(car["make"] + "|")
        file.write(car["model"] + "|")
        file.write(car["year"] + "|")
        file.write(car["color"] + "|")
        file.write(car["location"] + "|")
        file.write(car["notes"] + "\n")
    file.close()
    print("Cars saved to file!")

# Load cars from the text file
def load_cars():
    try:
        file = open("cars.txt", "r")
        for line in file:
            details = line.strip().split("|")
            if len(details) == 6:
                car = {
                    "make": details[0],
                    "model": details[1],
                    "year": details[2],
                    "color": details[3],
                    "location": details[4],
                    "notes": details[5]
                }
                cars.append(car)
        file.close()
        print("Cars loaded!")
    except FileNotFoundError:

        # Add some sample cars if there is no file yet
        cars.append({
            "make": "Porsche",
            "model": "911 GT3",
            "year": "2023",
            "color": "Blue",
            "location": "Schaumburg",
            "notes": "Black wheels and rear wing"
        })
        cars.append({
            "make": "Chevrolet",
            "model": "Corvette C8",
            "year": "2024",
            "color": "Black",
            "location": "Chicago",
            "notes": "Red interior"
        })
        cars.append({
            "make": "Ferrari",
            "model": "488 GTB",
            "year": "2019",
            "color": "Red",
            "location": "Rosemont",
            "notes": "Parked outside a shopping center"
        })

# Display the menu
def menu():
    print("\n==============================")
    print("     CAR SPOTTING DATABASE")
    print("==============================")
    print("1. Add a Car")
    print("2. View All Cars")
    print("3. Find a Car")
    print("4. Delete a Car")
    print("5. Save Cars to File")
    print("6. Quit")
    print("==============================")

# Main program
def main():
    load_cars()
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_car()
        elif choice == "2":
            view_cars()
        elif choice == "3":
            find_car()
        elif choice == "4":
            delete_car()
        elif choice == "5":
            save_cars()
        elif choice == "6":
            save_cars()
            print("Thanks for using the Car Spotting Database!")
            break
        else:
            print("Invalid choice. Try again.")
# Start the program
main()
