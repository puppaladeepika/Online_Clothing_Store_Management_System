#code 

import pandas as pd

# Initialize the DataFrame with sample data
clothes = [
    {"Id": 1100, "Name": "Dresses", "Available": 80, "Price": 899, "Original_Price": 999},
    {"Id": 1111, "Name": "Jeans", "Available": 40, "Price": 990, "Original_Price": 1090},
    {"Id": 1122, "Name": "Sarees", "Available": 100, "Price": 1050, "Original_Price": 1100},
    {"Id": 1133, "Name": "Shirts", "Available": 80, "Price": 750, "Original_Price": 800},
    {"Id": 1144, "Name": "Kurtas", "Available": 60, "Price": 599, "Original_Price": 650}
]


def adminLogin(): # Display admin login interface.
    print("--")
    print("---  Admin Online Clothing Store Management ---")
    print("1. Display the Catalog")
    print("2. Add Item")
    print("3. Update Item")
    print("4. Remove Item")
    print("5. Total Available Products")
    print("6. Logout")
    print("---")
    print("--")

def adminDisplayCatalog(cloth):  # Display current admin catalog.
    print("\nCurrent Admin Catalog:")
    print(cloth)
  
def add_item(cloth):
    # Add a new item to the catalog.
    new_id = int(input("Enter the new Id: "))  # Prompt user to enter the ID of the new item.
    new_name = input("Enter the new Name: ")  # Prompt user to enter the name of the new item.
    new_available = int(input("Enter quantity Available: "))  # Prompt user to enter the available quantity of the new item.
    new_price = int(input("Enter the Price: "))  # Prompt user to enter the price of the new item.
    new_original = int(input("Enter the Original Price: "))  # Prompt user to enter the original price of the new item.
    new_item = {"Id": new_id, "Name": new_name, "Available": new_available, "Price": new_price, "Original_Price": new_original}  # Create a dictionary for the new item.
    return cloth._append(new_item, ignore_index=True)  # Append the new item to the catalog DataFrame.

def update_item(cloth):
    # Update an existing item in the catalog.
    item_id = int(input("Enter the Id to be updated: "))  # Prompt user to enter the ID of the item to be updated.
    found = cloth['Id'] == item_id  # Check if the item with the provided ID exists in the catalog.
    if found.any():
        print("What do you want to update?")  # Prompt user to choose what aspect of the item to update.
        print("1. Name")
        print("2. Available")
        print("3. Price")
        print("4. Original_Price")
        choice = input("Choose an option: ")  # User selects an option.

        if choice == "1":
            new_name = input("Enter the new Name: ")  # Prompt user to enter the new name.
            cloth.loc[found, 'Name'] = new_name  # Update the name of the item.
        elif choice == "2":
            new_available = int(input("Enter the new Available: "))  # Prompt user to enter the new available quantity.
            cloth.loc[found, 'Available'] = new_available  # Update the available quantity.
        elif choice == "3":
            new_price = int(input("Enter the new Price: "))  # Prompt user to enter the new price.
            cloth.loc[found, 'Price'] = new_price  # Update the price of the item.
        elif choice == "4":
            new_original = int(input("Enter the new Original Price: "))  # Prompt user to enter the new original price.
            cloth.loc[found, 'Original_Price'] = new_original  # Update the original price of the item.
        else:
            print("Invalid choice.")  # Display message for invalid choice.
    else:
        print(f"Item with Id {item_id} not found.")  # Display message if the item is not found in the catalog.

    return cloth  # Return the updated catalog DataFrame.

def remove_item(cloth):
    # Remove an item from the catalog.
    item_id = int(input("Enter the valid Id of the item to be removed: "))  # Prompt user to enter the ID of the item to be removed.
    found = cloth['Id'] == item_id  # Check if the item with the provided ID exists in the catalog.
    if found.any():
        cloth = cloth[cloth['Id'] != item_id]  # Remove the item with the specified ID from the catalog.
        print(f"Item with Id {item_id} is removed successfully...")  # Display success message.
    else:
        print(f"Item with Id {item_id} is not found!!")  # Display message if the item is not found in the catalog.
    return cloth  # Return the updated catalog DataFrame.

def total_products_available(cloth):
    # Calculate and display the total quantity of available products.
    total = cloth['Available'].sum()  # Sum up the 'Available' column to get the total quantity of available goods.
    print(f"Total quantity of available goods are : {total}")  # Print the total quantity of available goods.

def adminChoice():
    # Allow the admin to perform various actions on the catalog.
    cloth_df = pd.DataFrame(clothes)  # Create a DataFrame from the initial catalog data.
    while True:
        adminLogin()  # Display the admin login interface.
        choice = input("Enter your choice: ")  # Prompt the admin to enter their choice.

        if choice == "1":
            adminDisplayCatalog(cloth_df)  # Display the current catalog to the admin.
        elif choice == "2":
            cloth_df = add_item(cloth_df)  # Add a new item to the catalog.
        elif choice == "3":
            cloth_df = update_item(cloth_df)  # Update an existing item in the catalog.
        elif choice == "4":
            cloth_df = remove_item(cloth_df)  # Remove an item from the catalog.
        elif choice == "5":
            total_products_available(cloth_df)  # Display the total quantity of available products.
        elif choice == "6":
            print("Logging out. Goodbye!!")  # Log out the admin and exit the loop.
            break
        else:
            print("Invalid choice. Please try again...")  # Display a message for invalid choices.
          

def userLogin():  # Display user login interface.
    print("--")
    print("--- User Online Clothes Shopping ---")
    print("1. Display The User Catalog")
    print("2. Place an Order and Checkout")
    print("3. Cancel an Order")
    print("4. Logout")
    print("--")

def userDisplayCatalog(cloth):  # Display current user catalog.
    print("\nCurrent Catalog:")
    print(cloth)
    
def placeOrder(cloth):
    # Allow the user to place an order for items from the catalog.
    total_amount = 0  # Initialize total amount variable.
    print("\nYour Cart:")
    print(f'Id\tName\tPrice\tOrdered Quantity')  # Print cart header.
    print("--")

    while True:
        order_id = int(input("Enter the Id of the item to place an order (0 to finish): "))  # Prompt user to enter item ID or finish the order.
        if order_id == 0:
            break  # Exit the loop if user finishes the order.
        found = cloth[cloth['Id'] == order_id]  # Find the item in the catalog based on ID.
        
        if not found.empty:  # Check if item exists in catalog.
            item_name = found.iloc[0]['Name']  # Get item name.
            available_quantity = found.iloc[0]['Available']  # Get available quantity.
            quantity_to_order = int(input(f"How many units of '{item_name}' would you like to order? Available quantity: {available_quantity}: "))  # Prompt user for quantity.
            
            if quantity_to_order > 0:  # Check if quantity ordered is positive.
                if available_quantity >= quantity_to_order:  # Check if sufficient quantity is available.
                    print(f'{order_id}\t{item_name}\t{found.iloc[0]["Price"]}\t{quantity_to_order}')  # Print order details.
                    total_amount += found.iloc[0]["Price"] * quantity_to_order  # Update total amount.
                    found_index = found.index[0]
                    cloth.loc[found_index, 'Available'] -= quantity_to_order  # Update available quantity in catalog.
                    print(f"Successfully placed the order for {quantity_to_order} units of '{item_name}'.")  # Confirm order placement.
                else:
                    print("Insufficient quantity available.")  # Display message for insufficient quantity.
            else:
                print("Order placement cancelled.")  # Display message if order placement is cancelled.
        else:
            print(f"Item with Id {order_id} not found.")  # Display message if item is not found in catalog.

    print(f"\nTotal amount to be paid: {total_amount}") #Display messsage with total amount 
    return cloth  # Return the updated catalog DataFrame

def cancelOrder(cloth, initial_quantities):
    # Allow the user to cancel an order.
    order_id = int(input("Enter the Id of the item to cancel the order: "))  # Prompt user to enter the ID of the item to cancel the order.
    found = cloth[cloth['Id'] == order_id]  # Find the item in the catalog based on ID.
    
    if not found.empty:  # Check if item exists in catalog.
        item_name = found.iloc[0]['Name']  # Get item name.
        ordered_quantity = found.iloc[0]['Available']  # Get ordered quantity.
        confirm = input(f"Cancel order for '{item_name}' (Id: {order_id})? (Y/N): ")  # Confirm order cancellation.
        
        if confirm.lower() == 'y':  # Check if user confirms order cancellation.
            found_index = found.index[0]
            cloth.loc[found_index, 'Available'] = initial_quantities[order_id]  # Restore initial available quantity.
            print(f"Order for '{item_name}' (Id: {order_id}) is cancelled.")  # Confirm order cancellation.
        else:
            print("Order cancellation cancelled.")  # Display message if order cancellation is cancelled.
    else:
        print(f"Item with Id {order_id} not found.")  # Display message if item is not found in catalog.

    return cloth  # Return the updated catalog DataFrame.

def logout():
    # Log out the user and exit the loop.
    print("Logging out. Goodbye!!")  # Display logout message.

def userChoice():
    # Allow the user to choose different actions in the user interface.
    cloth_df = pd.DataFrame(clothes)  # Create a DataFrame from the initial catalog data.
    initial_quantities = {row["Id"]: row["Available"] for _, row in cloth_df.iterrows()}  # Create a dictionary to store initial quantities.
    
    while True:
        userLogin()  # Display the user login interface.
        choice = input("Enter your choice: ")  # Prompt the user to enter their choice.

        if choice == "1":
            userDisplayCatalog(cloth_df)  # Display the current catalog to the user.
        elif choice == "2":
            cloth_df = placeOrder(cloth_df)  # Allow the user to place an order.
        elif choice == "3":
            cloth_df = cancelOrder(cloth_df, initial_quantities)  # Allow the user to cancel an order.
        elif choice == "4":
            logout()  # Log out the user and exit the loop.
            break
        else:
            print("Invalid choice. Please try again...")  # Display a message for invalid choices.
            
def createAccount():
    # Allow the user to create an account.
    print("Create an Account")  # Display account creation prompt.
    user_type = input("Are you a User or Admin? (U/A): ").lower()  # Prompt user to specify account type.
    
    if user_type == 'u':
        print("User account created successfully!")  # Display success message for user account creation.
    elif user_type == 'a':
        print("Admin account created successfully!")  # Display success message for admin account creation.
    else:
        print("Invalid option. Please choose U for User or A for Admin.")  # Display message for invalid option.

def login():
    # Allow the user to login with existing credentials.
    tp = input("Admin/User [A/U] : ")  # Prompt user to specify user type.
    
    if tp == 'A' or tp == 'a':
        password = input("Enter the password : ")  # Prompt user to enter password.
        if password == "admin":  # Check if password matches for admin.
            adminChoice()  # Redirect to admin menu.
        else:
            print("Invalid password. Please enter valid password")  # Display message for invalid password.

    elif tp == 'U' or tp == 'u':
        password = input("Enter the password : ")  # Prompt user to enter password.
        if(password == "user"):  # Check if password matches for user.
            userChoice()  # Redirect to user menu.
        else:
            print("Invalid password. Please enter valid password")  # Display message for invalid password.
    else:
        print("Invalid user type. Enter valid user type")  # Display message for invalid user type.

def loginOrCreateAccount():
    # Provide options for login or account creation.
    while True:
        print("--- Welcome to Online Clothing Store ---")  # Display welcome message.
        print("1. Login")  # Option for login.
        print("2. Create an Account")  # Option for account creation.
        print("3. Exit")  # Option to exit.
        choice = input("Enter your choice: ")  # Prompt user to enter choice.

        if choice == "1":
            login()  # Redirect to login function.
        elif choice == "2":
            createAccount()  # Redirect to account creation function.
        elif choice == "3":
            print("Exiting. Goodbye!")  # Display exit message.
            break  # Exit the loop.
        else:
            print("Invalid choice. Please try again.")  # Display message for invalid choice.
loginOrCreateAccount()
