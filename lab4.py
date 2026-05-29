# =============================================================================
# Student Name:Anthia Gardner-Celestine
# Lab Title: Lab 4 - Food Truck Order Queue
# Date: 5/26/2026
# =============================================================================

# Task 1.1: Create two lists

order_queue = []

menu = [
    "burger",
    "hot dog",
    "fries",
    "fried chicken wings",
    "buffalo wings",
    "soda",
    "bottled water",
    "local drink"
]

# 2.1 Display a welcome message
print("-----Welcome to our Food Truck!-----")

while True:
    print("\nType 'menu' to see what is available.")
    print("Type 'done' to complete your order.")
    print("Please enter items one at a time.")

    userinput = input("Enter the food item you want to order > ")

    # 2.2 If the user input is done, break out of the loop
    if userinput == "done":
        break

    # 2.3 If the user input is empty, continue to the start of the loop
    elif userinput == "":
        continue

    # Show menu
    elif userinput == "menu":
        print("Please choose from this menu:")
        for item in menu:
            print(f"- {item}")
        continue

    # 2.4 Check if the user input is on the menu
    elif userinput not in menu:
        print("Invalid choice")
        continue

    # 2.5 If it is on the menu, ask for quantity
    else:
        try:
            quantity = int(input(f"How many {userinput} would you like > "))
        except ValueError:
            print("Invalid quantity entered. Choose again.")
            continue

        for i in range(quantity):
            order_queue.append(userinput)

        print(f"Added {userinput} x {quantity} to order queue")


# Task 3: Process the order queue

# 3.1 Display the order queue to be processed
print(f"\nOriginal Order Queue: {order_queue}")
print("\n--- Processing Orders as follows...")

while order_queue:
    item = order_queue.pop(0)
    print(f"Fulfilling: {item} ({len(order_queue)} items remaining)")

print("All order entries were fulfilled successfully")


