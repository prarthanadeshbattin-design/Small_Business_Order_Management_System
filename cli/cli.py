from core.products import view_products, add_product, search_product, update_product, delete_product
from core.customers import view_customers, add_customer, search_customer, update_customer, delete_customer
from core.orders import create_order, read_orders_from_csv, update_order_status, cancel_order
from core.sales import daily_sales_summary, monthly_sales_summary   

def main_menu():
    print("Welcome to the Order Management System")
    print("1. Product")
    print("2. Customers") 
    print("3. Orders")
    print("4. Sales")
    print("5. Exit")
    input_choice = input("Enter your choice (1-5): ")
    while input_choice not in ['1', '2', '3', '4', '5']:
        print("Invalid choice. Please select a valid option.")
        input_choice = input("Enter your choice (1-5): ")
    return input_choice


def product_menu():
    while True: 
        print("Product Menu")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Back to Main Menu")
        input_choice = input("Enter your choice (1-6): ")
        while input_choice not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid choice. Please select a valid option.")
            input_choice = input("Enter your choice (1-6): ")

        if input_choice == '1':
            print("Add New Product")
            product_id = input("Enter Product ID: ")
            product_name = input("Enter Product Name: ")
            price = float(input("Enter Product Price: "))
            quantity = int(input("Enter Product Quantity: "))
            add_product("data/products.csv", product_id, product_name, price, quantity)
            print("Product added successfully!")
        elif input_choice == '2':
            products = view_products("data/products.csv")
            print(products)
        elif input_choice == '3':
            product_id = input("Enter Product ID to search: ")
            product = search_product("data/products.csv", product_id)
            if product:
                print(product)
        elif input_choice == '4':
            product_id = input("Enter Product ID to update: ")
            product = search_product("data/products.csv", product_id)
            if product:
                print("Product found. Please enter the new details.")
                product_name = input("Enter Product Name: ")
                price = float(input("Enter Product Price: "))
                quantity = int(input("Enter Product Quantity: "))
                update_product("data/products.csv", product_id, product_name, price, quantity)
                print("Product updated successfully!")
            else:
                print("Product not found.")
        elif input_choice == '5':
            product_id = input("Enter Product ID to delete: ")
            delete_product("data/products.csv", product_id)
            print("Product deleted successfully!")
        elif input_choice == '6':
            break

def run_cli():
    while True:
        choice = main_menu()
        if choice == '1':
            product_menu()
        elif choice == '2':
            customer_menu()
        elif choice == '3':
            order_menu()
        elif choice == '4':
            sales_menu()
        elif choice == '5':
            print("Exiting the Order Management System. Goodbye!")
            break

def customer_menu():
    while True:
        print("Customer Menu")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Search Customer")
        print("4. Update Customer")
        print("5. Delete Customer")
        print("6. Back to Main Menu")
        input_choice = input("Enter your choice (1-6): ")
        while input_choice not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid choice. Please select a valid option.")
            input_choice = input("Enter your choice (1-6): ")

        if input_choice == '1':
            print("Add New Customer")
            customer_id = input("Enter Customer ID: ")
            customer_name = input("Enter Customer Name: ")
            phone = input("Enter Customer Phone: ")
            email = input("Enter Customer Email: ")
            add_customer("data/customers.csv", customer_id, customer_name, phone, email)
            print("Customer added successfully!")
        elif input_choice == '2':
            customers = view_customers("data/customers.csv")
            print(customers)
        elif input_choice == '3':
            search_term = input("Enter search term (ID, Name, Phone, or Email): ")
            matching_customers = search_customer("data/customers.csv", search_term)
            if matching_customers:
                for customer in matching_customers:
                    print(customer)
            else:
                print("No matching customers found.")
        elif input_choice == '4':
            customer_id = input("Enter Customer ID to update: ")
            updated_info = {}
            new_name = input("Enter new name (leave blank to keep current): ")
            if new_name:
                updated_info['customer_name'] = new_name
            new_phone = input("Enter new phone (leave blank to keep current): ")
            if new_phone:
                updated_info['phone'] = new_phone
            new_email = input("Enter new email (leave blank to keep current): ")
            if new_email:
                updated_info['email'] = new_email
            update_customer("data/customers.csv", customer_id, updated_info)
            print("Customer updated successfully!")
        elif input_choice == '5':
            customer_id = input("Enter Customer ID to delete: ")
            delete_customer("data/customers.csv", customer_id)
            print("Customer deleted successfully!")
        elif input_choice == '6':
            break

def order_menu():
    while True:
        print("Order Menu")
        print("1. Create Order")
        print("2. View Orders")
        print("3. Update Order Status")
        print("4. Cancel Order")
        print("5. Back to Main Menu")
        input_choice = input("Enter your choice (1-5): ")
        while input_choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice. Please select a valid option.")
            input_choice = input("Enter your choice (1-5): ")   

        if input_choice == '1':
            print("Create New Order")
            order_id = input("Enter Order ID: ")
            customer_id = input("Enter Customer ID: ")
            product_id = input("Enter Product ID: ")
            quantity = int(input("Enter Quantity: "))
            date = input("Enter Order Date (YYYY-MM-DD): ")
            status = 'Pending'
            create_order("data/orders.csv", "data/customers.csv", "data/products.csv", order_id, customer_id, product_id, quantity, date, status)
            print("Order created successfully!")
        elif input_choice == '2':
            orders = read_orders_from_csv("data/orders.csv")
            if orders:
                for order in orders:
                    print(order)
            else:
                print("No orders found.")
        elif input_choice == '3':
            print("Update Order Status")
            order_id = input("Enter order ID:")
            new_status = input("Enter New Status (Pending/Processing/Completed): ")
            update_order_status("data/orders.csv", order_id, new_status)
            print("Order status updated successfully!")
        elif input_choice == '4':
            print("Cancel Order")
            order_id = input("Enter order ID:")
            cancel_order("data/orders.csv", order_id, "data/products.csv")
            print("Order cancelled successfully!")
        elif input_choice == '5':
            break

def sales_menu():
    while True:
        print("Sales Menu")
        print("1. Daily Sales Summary")
        print("2. Monthly Sales Summary")
        print("3. Back to Main Menu")
        input_choice = input("Enter your choice (1-3): ")
        while input_choice not in ['1', '2', '3']:
            print("Invalid choice. Please select a valid option.")
            input_choice = input("Enter your choice (1-3): ")

        if input_choice == '1':
            try:
                date = input("Enter date for daily sales summary (YYYY-MM-DD): ")
                summary = daily_sales_summary("data/orders.csv", date)
                print(summary)
            except ValueError as e:
                print("Error:", e)
        elif input_choice == '2':
            try:
                month = int(input("Enter month for monthly sales summary (1-12): "))
                year = int(input("Enter year for monthly sales summary (e.g., 2024): "))
                summary = monthly_sales_summary("data/orders.csv", month, year)
                print(summary)
            except ValueError as e:
                print("Error:", e)
        elif input_choice == '3':
            break

