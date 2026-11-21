import csv

def read_products_from_csv(file_path):
    products = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            product = {
                'product_id': row['product_id'],
                'product_name': row['product_name'],
                'price': float(row['price']),
                'quantity': int(row['quantity'])
            }
            products.append(product)
    return products


def save_products_to_csv(products, file_path):
    with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['product_id', 'product_name', 'price', 'quantity']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for product in products:
            writer.writerow({
                'product_id': product['product_id'],
                'product_name': product['product_name'],
                'price': product['price'],
                'quantity': product['quantity']
            })


def add_product(file_path, product_id, product_name, price, quantity):

    if not product_id or not product_name or price is None or quantity is None:
        raise ValueError("All product fields must be provided.")

    if not isinstance(price, (int, float)) or price <= 0:
        raise ValueError("Price must be greater than zero number.")
    if not isinstance(quantity, int) or quantity < 0:
        raise ValueError("Quantity must be a non-negative integer.")
    
    products = read_products_from_csv(file_path)

    for product in products:
        if product['product_id'] == product_id:
            raise ValueError(f"Product with ID {product_id} already exists.")

    product = {
        'product_id': product_id,
        'product_name': product_name,
        'price': price,
        'quantity': quantity
    }
    products.append(product)
    save_products_to_csv(products, file_path)

def view_products(file_path):
    products = read_products_from_csv(file_path)
    return products

def search_product(file_path, search_term):
    products = read_products_from_csv(file_path)
    matching_products = []  
    for product in products:
        if search_term.lower() in product['product_id'].lower() or search_term.lower() in product['product_name'].lower():
            matching_products.append(product)
    return matching_products

def update_product(file_path, product_id, new_name=None, new_price=None, new_quantity=None):  
    
    products = read_products_from_csv(file_path)
    product_found = False

    for product in products:
        if product['product_id'] == product_id:
            product_found = True
            if new_name is not None:
                product['product_name'] = new_name
            if new_price is not None:
                if not isinstance(new_price, (int, float)) or new_price <= 0:
                    raise ValueError("Price must be greater than zero number.")
                product['price'] = new_price
            if new_quantity is not None:
                if not isinstance(new_quantity, int) or new_quantity < 0:
                    raise ValueError("Quantity must be a non-negative integer.")
                product['quantity'] = new_quantity
            break

    if not product_found:
        raise ValueError(f"Product with ID {product_id} not found.")

    save_products_to_csv(products, file_path) 

def delete_product(file_path, product_id):
    products = read_products_from_csv(file_path)
    product_found = False

    for i, product in enumerate(products):
        if product['product_id'] == product_id:
            product_found = True
            del products[i]
            break

    if not product_found:
        raise ValueError(f"Product with ID {product_id} not found.")

    save_products_to_csv(products, file_path)   