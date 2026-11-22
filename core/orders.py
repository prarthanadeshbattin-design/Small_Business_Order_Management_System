import csv
import copy

from datetime import datetime
from .customers import read_customers_from_csv
from .products import read_products_from_csv, save_products_to_csv

def read_orders_from_csv(file_path):
    orders = []
    try:
        with open(file_path, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                orders.append(row)
    except FileNotFoundError:
        pass  # If the file doesn't exist, return an empty list
    return orders   

def save_orders_to_csv(orders, file_path):
    with open(file_path, mode='w', newline='') as csvfile:
        fieldnames = ['order_id', 'customer_id', 'product_id', 'quantity', 'total', 'date', 'status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)    
        writer.writeheader()
        for order in orders:
            writer.writerow(order)

def create_order(file_path, customer_file_path, product_file_path, order_id, customer_id, product_id, quantity, date, status):

    if not order_id or not customer_id or not product_id or not date or not status:
        raise ValueError("All order fields must be provided.")

    if not isinstance(date, str):
        raise ValueError("Date must be in YYYY-MM-DD format.")

    try:
        parsed_date = datetime.strptime(date, '%Y-%m-%d')

        if parsed_date.strftime('%Y-%m-%d') != date:
            raise ValueError("Date must be in YYYY-MM-DD format.")

    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format.")
   
    allowed_statuses = ['Pending', 'Processing', 'Completed', 'Cancelled']

    if status not in allowed_statuses:
        raise ValueError("Invalid order status.")

    orders = read_orders_from_csv(file_path)
    original_orders = copy.deepcopy(orders)

    for existing_order in orders:
        if existing_order['order_id'] == order_id:

            if existing_order['customer_id'] != customer_id:
                raise ValueError("Order ID already belongs to another customer.")

            if existing_order['date'] != date or existing_order['status'] != status:
                raise ValueError("Order details do not match the existing order.")

            if existing_order['product_id'] == product_id:
                raise ValueError("This product is already added to the order.")

    if type(quantity) is not int or quantity <= 0:
        raise ValueError("Quantity must be a positive integer.")

    customers = read_customers_from_csv(customer_file_path)

    if not any(customer['customer_id'] == customer_id for customer in customers):
        raise ValueError(f"Customer with ID {customer_id} does not exist.")

    products = read_products_from_csv(product_file_path)
    original_products = copy.deepcopy(products)

    if not any(product['product_id'] == product_id for product in products):
        raise ValueError(f"Product with ID {product_id} does not exist.")

    product = next((p for p in products if p['product_id'] == product_id), None)    

    if quantity > int(product['quantity']):
        raise ValueError("Insufficient stock available.")

    total = float(product['price']) * quantity

    product['quantity'] = int(product['quantity']) - quantity

    order = {
        'order_id': order_id,
        'customer_id': customer_id,
        'product_id': product_id,
        'quantity': quantity,
        'total': total,
        'date': date,
        'status': status
    }
    
    orders.append(order)

    try:             
        save_orders_to_csv(orders, file_path)   
        save_products_to_csv(products, product_file_path)
    except Exception:
        save_orders_to_csv(original_orders, file_path)
        save_products_to_csv(original_products, product_file_path)
        raise
        
    return order