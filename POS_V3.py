# This command-line point-of-sale program lets a cashier add products and prices
# to a list, display every stored product with the total, clear the screen, and
# quit. Each POS action is handled by a function. The menu repeats in a for loop
# until the user enters "Q", which is the loop's sentinel value.

import os


# Ask the cashier what action to perform and return the choice in lowercase.
def get_choice():
    print("\nPoint of Sale")
    print("A - Add a product")
    print("R - Show all products and the total")
    print("C - Clear the screen")
    print("Q - Quit")
    return input("Choose an option: ").strip().lower()


# Ask for a product name and price, then store both together in the products list.
def add_product(products):
    name = input("Enter the product name: ").strip()

    if not name:
        print("The product name cannot be empty.")
        return

    try:
        price = float(input("Enter the product price: R"))
    except ValueError:
        print("Please enter a valid price.")
        return

    if price < 0:
        print("The price cannot be negative.")
        return

    products.append([name, price])
    print(f"{name} has been added.")


# Display every product saved in the list and add their prices to the total.
def show_products_and_total(products):
    print("\nProducts:")
    total = 0

    if not products:
        print("No products have been added.")

    for product in products:
        name = product[0]
        price = product[1]
        print(f"{name} R{price:.2f}")
        total = total + price

    print(f"Total: R{total:.2f}")


# Clear the Windows Command Prompt screen while keeping stored products.
def clear_screen():
    os.system("cls")


# Keep each stored product as a two-value list: its name and its price.
products = []

# Repeat the menu until "q" is entered; "q" is the sentinel value for this loop.
for choice in iter(get_choice, "q"):
    if choice == "a":
        add_product(products)
    elif choice == "r":
        show_products_and_total(products)
    elif choice == "c":
        clear_screen()
    else:
        print("Invalid option. Choose A, R, C, or Q.")

print("Goodbye!")