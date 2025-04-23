"""You are a student in a class of 10. Your class teacher assigns you a task of entering the
names of all the students in the class. You finally want to display the names given the
condition that the maximum allowed characters in a name is 15. As a fun task, reverse the
names and display them. [Hint: Slicing works when you are selecting maximum characters]"""

student_names = []

for i in range(3):
    name = input(f"Enter the name of student {i + 1}: ")

    student_names.append(name)

print("\nReversed names:")

for name in student_names:
    print(name[::-1])
