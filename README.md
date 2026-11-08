## Inventory
A command-line inventory manager written in Python. It stores products in a dictionary with a price and quantity for each, and runs an interactive menu loop for adding, removing, editing, searching, and valuing stock.

## Features
Add Product — Prompts for a name, price, and quantity, then stores the product in the inventory.

Remove Product — Deletes a product by name if it exists.

Change Price — Updates the price of an existing product.

Change Stock — Updates the quantity of an existing product.

Search Product — Looks up a product and prints its price and quantity.

View Products — Lists every product with its price and quantity.

Calculate Value — Multiplies price by quantity for every product and prints the total inventory value.

Input Validation — Re-prompts on non-numeric price and quantity input using try/except ValueError.

Menu Loop — Runs until the user selects option 8 to exit.

## Technologies Used
| Technology | Purpose |
|---|---|
| Python | Application logic |
| Dictionary (`inventory`) | Stores products and their details |
| Nested Dictionaries | Holds `price` and `quantity` per product |
| `input()` / `print()` | Console interaction |
| `float()` / `int()` | Parses price and quantity values |
| `try / except` | Handles invalid numeric input |
<!-- -->
## How to Use It
Install Python 3.6 or newer from python.org and make sure it's added to your PATH.

Save the code as inventory.py.

Open a terminal in the folder containing the file.

Run python inventory.py.

Use the menu: 1 to add, 2 to remove, 3 to change price, 4 to change stock, 5 to search, 6 to view all, 7 to calculate total value, 8 to exit.

## Improvements
Persist the inventory — Save the dictionary to a JSON file on exit and reload it on startup so products survive between sessions.

Fix price precision — change_price uses int() while add_product uses float(), so decimals are lost when editing a price; use float() in both, and format output with two decimal places.

