'''Write a program that asks the user to enter a length in feet. The program should then give
the user the option to convert from feet into inches, yards, miles, millimeters, centimeters,
meters, or kilometers. Say if the user enters a 1, then the program converts to inches, if they
enter a 2, then the program converts to yards, etc. While this can be done with if statements,
it is much shorter with lists and it is also easier to add new conversions if you use lists.'''

length = float(input("Enter length in terms of feet: ")) 
choice = int(input("Choose a conversion: \n1: Inches \n2: Yards \n3: Miles \n4: Millimeters \n5: Centimeters\n"))


a = [12 * length, 0.33 * length, 0.000189 * length, 304.8 * length, 30.48 * length]


if 1 <= choice <= 5:
    print("Ans:", a[choice - 1]) 
else:
    print("Invalid choice! Please enter a number between 1 and 5.")
