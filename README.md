Inventory Manager
A command-line Python program that lets a user add, remove, search, and update products in a simple inventory, plus calculate total stock value.

Concepts Used
Dictionaries — the inventory dict stores each product's price and quantity as nested key-value pairs.

Functions — each menu action is broken into its own reusable function.

Exception Handling — try/except blocks validate numeric input for price and quantity.

Features
Add & Remove Products — store new items or delete existing ones by name.

Update Price & Stock — change a product's price or quantity with confirmation messages.

Search & Totals — look up individual products or calculate the total inventory value.

Improvements
Persistent Storage — save the inventory to a file (e.g. JSON) so data isn't lost on exit.

Fix Price Input Bug — change_price() uses int() instead of float(), rejecting decimal prices.

Duplicate Check & Formatting — warn when adding an existing product and format currency to 2 decimal places.

