📦 Python Inventory Management Program
A simple command-line inventory management application built with Python. This program lets users add, remove, search, and update products in an inventory, as well as view all products and calculate the total stock value. It's a great beginner project for learning about dictionaries, nested data structures, and menu-driven programs in Python.

📖 Python Inventory Management Program
The Python Inventory Management Program is a console-based application that stores product information in a dictionary. Each product is stored by name, with a nested dictionary containing its price and quantity.

When the program starts, a looping menu appears with options to add a product, remove a product, change a product's price, change stock, search for a product, view all products, calculate total inventory value, or exit.

All numeric input (price and quantity) is wrapped in error handling, so invalid entries won't crash the program. The inventory is held in memory during the session, making this a clean and approachable example of how to manage structured data in Python.

✨ Features
Add a product – Enter a name, price, and quantity to add a new item.

Remove a product – Delete an item by name.

Change price – Update the price of an existing product.

Change stock – Update the quantity of an existing product.

Search for a product – Look up a product by name and view its details.

View all products – List every product with its price and quantity.

Calculate total inventory value – Sums price × quantity for all products.

Input validation – Rejects non-numeric prices and non-integer quantities.

Looping menu – Keeps running until the user chooses to exit.

Simple exit option – Quit the program cleanly at any time.

🛠️ What It Uses
Language & Library
Python 3 – No external libraries required (pure standard library).

Data Structure
python
inventory = {
    "product_name": {
        "price": float,
        "quantity": int
    }
}
Key Functions
Function	Purpose
add_product()	Prompts for a name, price, and quantity, then adds the product to the inventory.
remove_product()	Deletes a product by name if it exists.
change_price()	Updates the price of an existing product.
change_stock()	Updates the quantity of an existing product.
search_product()	Looks up a product and displays its price and quantity.
view_products()	Loops through and prints all products in the inventory.
calculate_value()	Multiplies price by quantity for each product and prints the total value.
Python Concepts Demonstrated
Dictionaries – Storing products and their details.

Nested dictionaries – Each product holds its own price and quantity.

Functions – Organizing logic into reusable blocks.

Conditional logic – Checking whether a product exists before modifying it.

Exception handling – try/except blocks for safe numeric input.

Loops – while True loops for the menu and input validation.

for loops with .items() – Iterating over dictionary entries.

User input – Reading and processing input via input().

Built-in Functions Used
input() – Reads user input from the console.

print() – Displays menus and product details.

float() – Converts input into a decimal number (for prices).

int() – Converts input into a whole number (for quantities).

del – Removes a product from the dictionary.

exit() – Terminates the program.

📥 Download
You can download the source file from this repository and save it as a .py file:

text
inventory.py
No installation or dependencies are needed — just Python.

▶️ How to Run
Make sure you have Python 3 installed (python.org).

Save the code as inventory.py.

Open a terminal or command prompt in the folder containing the file.

Run:

bash
python inventory.py
Use the menu to add, remove, search, update, or view products in your inventory.

