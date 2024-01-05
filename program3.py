#WAP to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.
class ShoppingCart:

    def __init__(self):
        self.items = []  # List to store items and their prices

    def add_item(self, item_name, item_price):
        self.items.append((item_name, item_price))
        print(f"{item_name} added to cart!")

    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:  # Find the item by name
                self.items.remove(item)
                print(f"{item_name} removed from cart!")
                return  # Exit the loop after removing
        print(f"{item_name} not found in cart.")

    def calculate_total(self):
        total_price = 0
        for item_name, item_price in self.items:
            total_price += item_price
        return total_price

# Create a shopping cart instance
my_cart = ShoppingCart()

# Get user input for items and prices
while True:
    action = input("What do you want to do? (add, remove, total, or quit): ")

    if action == "add":
        item_name = input("Enter item name: ")
        item_price = float(input("Enter item price: "))
        my_cart.add_item(item_name, item_price)

    elif action == "remove":
        item_name = input("Enter item name to remove: ")
        my_cart.remove_item(item_name)

    elif action == "total":
        total_price = my_cart.calculate_total()
        print("Total price:", total_price)

    elif action == "quit":
        break  # Exit the loop

    else:
        print("Invalid action. Please choose add, remove, total, or quit.")
