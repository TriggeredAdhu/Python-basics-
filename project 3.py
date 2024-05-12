# Project 3
# Get 5 student names and for each student get 5 subjects marks. Display the student name and total marks.

for i in range(5):
    name = (input("enter the student name:"))
    total = 0
    for j in range(5):
        marks = int(input("enter the mark of the student:"))
        total += marks
    print("the total mark of", name, "is", total)
