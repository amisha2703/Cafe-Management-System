# cafe management system
# using dictionary and conditional statement and loops

menu = {
    "pizza": 40,
    "maggi": 50,
    "coffee": 80,
    "pasta": 70,
    "samosa": 60
}

# Print menu items
print("Welcome to Python Restaurant")
print("pizza: rs40\nmaggi: rs50\ncoffee: rs80\npasta: rs70\nsamosa: rs60")

# Initialize total amount
order_total = 0

# Loop for ordering multiple items
while True:
    # Take input for item
    item = input("Enter the name of the item you want to order: ")

    # Check if item is in menu
    if item in menu:
        order_total += menu[item]
        print(f"Your item {item} has been added to your order.")
    else:
        print(f"Sorry, {item} is not available.")

    # Ask if user wants to add another item
    another_order = input("Do you want to add another item? (Yes/No): ")

    # Break the loop if the user does not want to add more items
    if another_order != "yes":
        break

# Display total order cost
print(f"The total amount to pay is: Rs {order_total}")
