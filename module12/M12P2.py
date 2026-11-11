# problem 2
# display student names and their exam scores

names = ["Anderson", "Bennett", "Whitaker", "Thompson", "Calloway",
         "Morrison", "Blackwell", "Garcia", "Hawthorne", "Miller"]
scores = [88, 94, 79, 91, 85, 76, 97, 82, 90, 87]

def display_names():
    print("student names and exam scores:")
    for i in range(10):
        print(names[i], scores[i])

def reverse_names():
    print("\nnames and scores in reverse order:")
    for i in range(9, -1, -1):
        print(names[i], scores[i])

# main program
display_names()
reverse_names()
