# problem 1
# display last names and then display them backwards

names = ["Anderson", "Bennett", "Whitaker", "Thompson", "Calloway",
         "Morrison", "Blackwell", "Garcia", "Hawthorne", "Miller"]
def display_names():
    print("here are the last names:")
    for i in range(10):
        print(names[i])

def reverse_names():
    print("\nnames in reverse order:")
    for i in range(9, -1, -1):
        print(names[i])

# main program
display_names()
reverse_names()
