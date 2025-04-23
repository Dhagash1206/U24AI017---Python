'''Write a program that repeatedly asks the user to enter product names and prices. Store all
of these in a dictionary whose keys are the product names and whose values are the prices.
When the user is done entering products and prices, allow them to repeatedly enter a
product name and print the corresponding price or a message if the product is not in the dictionary.'''

products = {}

while (1):
    print("\n1. Enter product and price details ?")
    print("2. Find product or price ?")
    print("3. Exit")
    choice = input("Choose an choice :")

    if choice == "1":
        p_name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        products[p_name] = price
    elif choice == "2":
        p_name = input("Enter product name: ")
        if p_name in products:
            print(f"Price of {p_name}: {products[p_name]}")
        else:
            print(f"{p_name} not found.")
    elif choice == "3":
        break
    else:
        print("Invalid option. Please choose again.")
