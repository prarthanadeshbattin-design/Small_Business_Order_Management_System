import csv


def read_customers_from_csv(file_path):
    customers = []
    try:
        with open(file_path, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                customers.append(row)
    except FileNotFoundError:
        pass  
    return customers

def save_customers_to_csv(customers, file_path):
    with open(file_path, mode='w', newline='') as csvfile:
        fieldnames = ['customer_id', 'customer_name', 'phone', 'email']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for customer in customers:
            writer.writerow(customer)

def add_customer(file_path, customer_id, customer_name, phone, email):
    if not customer_id or not customer_name or not phone or not email:
        raise ValueError("All customer fields must be provided.")

    customers = read_customers_from_csv(file_path)

    for customer in customers:
        if customer['customer_id'] == customer_id:
            raise ValueError(f"Customer with ID {customer_id} already exists.")

    customer = {
        'customer_id': customer_id,
        'customer_name': customer_name,
        'phone': phone,
        'email': email
    }
    customers.append(customer)
    save_customers_to_csv(customers, file_path)

def view_customers(file_path):
    customers = read_customers_from_csv(file_path)
    return customers

def search_customer(file_path, search_term):
    customers = read_customers_from_csv(file_path)
    matching_customers = []

    for customer in customers:
        if (search_term.lower() in customer['customer_id'].lower() or
            search_term.lower() in customer['customer_name'].lower() or
            search_term.lower() in customer['phone'].lower() or
            search_term.lower() in customer['email'].lower()):
            matching_customers.append(customer)
    return matching_customers

def update_customer(file_path, customer_id, updated_info):
    customers = read_customers_from_csv(file_path)
    customer_found = False

    for customer in customers:
        if customer['customer_id'] == customer_id:
            allowed_fields = ['customer_name', 'phone', 'email']

            if not updated_info or not all(key in allowed_fields for key in updated_info):
                raise ValueError("Invalid customer fields to update.")
            customer.update(updated_info)
            customer_found = True
            break

    if not customer_found:
        raise ValueError(f"Customer with ID {customer_id} not found.")

    save_customers_to_csv(customers, file_path)

def delete_customer(file_path, customer_id):
    customers = read_customers_from_csv(file_path)
    updated_customers = [customer for customer in customers if customer['customer_id'] != customer_id]

    if len(customers) == len(updated_customers):
        raise ValueError(f"Customer with ID {customer_id} not found.")

    save_customers_to_csv(updated_customers, file_path)
    