def display_menu():
    print("\n===============================")
    print("  WELCOME TO THE STATIONARY MANAGEMENT SYSTEM")
    print("        Created by: Devesh Dixit")
    print("===============================")
    print("1. View All Items")
    print("2. Add New Item")
    print("3. Update Item Quantity")
    print("4. Sell Item")
    print("5. View Item Details")
    print("6. Delete Item")
    print("7. Backup Data")
    print("8. Search Item by Name")
    print("9. View Low Stock Items")
    print("10. Calculate Total Inventory Value")
    print("11. Restock Item")
    print("12. Modify Item Price")
    print("13. Generate Sales Report")
    print("14. Exit")
    print("===============================")

def load_data():
    items = []
    try:
        with open("stationary_data.txt", "r") as file:
            for line in file:
                item = line.strip().split(",")
                items.append({"name": item[0], "price": float(item[1]), "quantity": int(item[2])})
    except FileNotFoundError:
        print("No previous data found, starting fresh.")
    return items

def save_data(items):
    with open("stationary_data.txt", "w") as file:
        for item in items:
            file.write(f"{item['name']},{item['price']},{item['quantity']}\n")

def backup_data(items):
    with open("backup_stationary_data.txt", "w") as file:
        for item in items:
            file.write(f"{item['name']},{item['price']},{item['quantity']}\n")
    with open("backup_purchase_records.txt", "w") as file:
        try:
            with open("purchase_records.txt", "r") as records_file:
                file.write(records_file.read())
        except FileNotFoundError:
            print("No purchase records to back up.")
    print("Data and purchase records backup completed successfully.")

def view_all_items(items):
    if len(items) == 0:
        print("No items available in the inventory.")
    else:
        print("\nItem List:")
        for item in items:
            print(f"Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}")

def add_new_item(items):
    name = input("Enter item name: ").strip()
    price = input("Enter item price: ").strip()
    quantity = input("Enter item quantity: ").strip()

    try:
        price = float(price)
        quantity = int(quantity)
    except ValueError:
        print("Invalid price or quantity. Please enter valid numeric values.")
        return

    items.append({"name": name, "price": price, "quantity": quantity})
    print(f"Item '{name}' added successfully!")

def update_item_quantity(items):
    name = input("Enter item name to update quantity: ").strip()
    found = False
    for item in items:
        if item['name'].lower() == name.lower():
            try:
                new_quantity = int(input(f"Enter new quantity for {item['name']}: ").strip())
                item['quantity'] = new_quantity
                print(f"Quantity updated for '{item['name']}' to {new_quantity}.")
                found = True
                break
            except ValueError:
                print("Please enter a valid number for quantity.")
                return
    if not found:
        print(f"Item '{name}' not found.")

def sell_item(items):
    name = input("Enter item name to sell: ").strip()
    found = False
    for item in items:
        if item['name'].lower() == name.lower():
            try:
                quantity_to_sell = int(input(f"Enter quantity to sell for {item['name']}: ").strip())
                if quantity_to_sell <= item['quantity']:
                    item['quantity'] -= quantity_to_sell
                    total_price = quantity_to_sell * item['price']
                    print(f"Sold {quantity_to_sell} of {item['name']}. Total price: {total_price}.")
                    save_purchase_record(item['name'], quantity_to_sell, total_price)
                    found = True
                    break
                else:
                    print("Not enough stock available to sell.")
            except ValueError:
                print("Please enter a valid number for quantity.")
                return
    if not found:
        print(f"Item '{name}' not found.")

def save_purchase_record(item_name, quantity, total_price):
    with open("purchase_records.txt", "a") as file:
        file.write(f"Item: {item_name}, Quantity: {quantity}, Total Price: {total_price:.2f}\n")

def view_item_details(items):
    name = input("Enter item name to view details: ").strip()
    found = False
    for item in items:
        if item['name'].lower() == name.lower():
            print(f"Item details:\nName: {item['name']}\nPrice: {item['price']}\nQuantity: {item['quantity']}")
            found = True
            break
    if not found:
        print(f"Item '{name}' not found.")

def delete_item(items):
    name = input("Enter item name to delete: ").strip()
    found = False
    for i, item in enumerate(items):
        if item['name'].lower() == name.lower():
            items.pop(i)
            print(f"Item '{name}' deleted successfully.")
            found = True
            break
    if not found:
        print(f"Item '{name}' not found.")

def search_item_by_name(items):
    search_name = input("Enter item name to search for: ").strip()
    found_items =[item for item in items if search_name.lower() in item['name'].lower()]
    if found_items:
        print("\nSearch Results:")
        for item in found_items:
            print(f"Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}")
    else:
        print(f"No items found matching '{search_name}'.")

def view_low_stock_items(items):
    threshold = input("Enter stock threshold: ").strip()
    try:
        threshold = int(threshold)
    except ValueError:
        print("Please enter a valid number for threshold.")
        return
    
    low_stock_items = [item for item in items if item['quantity'] <= threshold]
    if low_stock_items:
        print("\nLow Stock Items:")
        for item in low_stock_items:
            print(f"Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}")
    else:
        print("No items are below the specified threshold.")

def calculate_inventory_value(items):
    total_value = sum(item['price'] * item['quantity'] for item in items)
    print(f"\nTotal inventory value: {total_value:.2f}")

def restock_item(items):
    name = input("Enter item name to restock: ").strip()
    found = False
    for item in items:
        if item['name'].lower() == name.lower():
            try:
                restock_quantity = int(input(f"Enter quantity to restock for {item['name']}: ").strip())
                item['quantity'] += restock_quantity
                print(f"Restocked {restock_quantity} for {item['name']}. New quantity: {item['quantity']}")
                found = True
                break
            except ValueError:
                print("Please enter a valid number for quantity.")
                return
    if not found:
        print(f"Item '{name}' not found.")

def modify_item_price(items):
    name = input("Enter item name to modify price: ").strip()
    found = False
    for item in items:
        if item['name'].lower() == name.lower():
            try:
                new_price = float(input(f"Enter new price for {item['name']}: ").strip())
                item['price'] = new_price
                print(f"Price for '{item['name']}' updated to {new_price}.")
                found = True
                break
            except ValueError:
                print("Please enter a valid number for price.")
                return
    if not found:
        print(f"Item '{name}' not found.")

def generate_sales_report():
    try:
        with open("purchase_records.txt", "r") as file:
            records = file.readlines()
            if records:
                print("\nSales Report:")
                for record in records:
                    print(record.strip())
            else:
                print("No sales records found.")
    except FileNotFoundError:
        print("No sales records found.")

def main():
    items = load_data()
    
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            view_all_items(items)
        elif choice == '2':
            add_new_item(items)
        elif choice == '3':
            update_item_quantity(items)
        elif choice == '4':
            sell_item(items)
        elif choice == '5':
            view_item_details(items)
        elif choice == '6':
            delete_item(items)
        elif choice == '7':
            backup_data(items)
        elif choice == '8':
            search_item_by_name(items)
        elif choice == '9':
            view_low_stock_items(items)
        elif choice == '10':
            calculate_inventory_value(items)
        elif choice == '11':
            restock_item(items)
        elif choice == '12':
            modify_item_price(items)
        elif choice == '13':
            generate_sales_report()
        elif choice == '14':
            save_data(items)
            print("Exiting system... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
