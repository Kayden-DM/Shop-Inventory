inventory = {}
 
 
def add_product():
    name = input("Product name: ")
 
    while True:
        try:
            price = float(input("Price: $ "))
            break
        except ValueError:
            print("Please enter a valid number.")
 
    while True:
        try:
            quantity = int(input("Quantity: "))
            break
        except ValueError:
            print("Please enter a whole number.")
 
    inventory[name] = {
        "price":price,
        "quantity":quantity
    }
 
 
def remove_product():
    name = input("What product do you want to remove? ")
 
    if name in inventory:
        del inventory[name]
        print("Product removed.")
    else:
        print("Product not found.")
 

def change_price():
    name = input("What price would you like to change? ")

    if name in inventory:
        while True:
            try:
                price = int(input("New price: "))
                break
            except ValueError:
                print("Please enter a whole number.")
        inventory[name]["price"] = price
        print("price updated.")
    else:
        print("Product not found.")

 
def change_stock():
    name = input("What quantity would you like to change? ")

    if name in inventory:
        while True:
            try:
                quantity = int(input("New quantity: "))
                break
            except ValueError:
                print("Please enter a whole number.")
        inventory[name]["quantity"] = quantity
        print("Stock updated.")
    else:
        print("Product not found.")
 
 
def search_product():
    name = input("What product are you searching for? ")
 
    if name in inventory:
        print("Product found.")
        print("Price: $", inventory[name]["price"])
        print("Quantity: ", inventory[name]["quantity"])
    else:
        print("Product not found.")
 
 
def view_products():
    for name, details in inventory.items():
        print(name)
        print("Price: $", details["price"])
        print("Quantity: ", details["quantity"])
        print()
 
 
def calculate_value():
    total = 0
 
    for name, details in inventory.items():
        value = details["price"] * details["quantity"]
        total += value
 
    print("The total inventory value is: $", total)
 
 
while True:
    print("          INVENTORY         ")
    print(" 1. Add product.")
    print(" 2. Remove product.")
    print(" 3. Change price.")
    print(" 4. Change stock.")
    print(" 5. Search for product.")
    print(" 6. View products.")
    print(" 7. Calculate stock value.")
    print(" 8. Exit.")
 
    choice = input("Choose an option: ")
 
    if choice == "1":
        add_product()
        
    elif choice == "2":
        remove_product()
    
    elif choice == "3":
        change_price()
 
    elif choice == "4":
        change_stock()
 
    elif choice == "5":
        search_product()
 
    elif choice == "6":
        view_products()
        
    elif choice == "7":
        calculate_value()
        
    elif choice == "8":
        exit()
 
    else:
        print("Invalid option.")