from datetime import datetime
from .orders import read_orders_from_csv

def daily_sales_summary(file_path, date):
    datetime.strptime(date, '%Y-%m-%d')
    orders = read_orders_from_csv(file_path)
    total_sales = 0
    total_items_sold = 0
    order_ids = set()

    for order in orders:
        if order['date'] == date and order['status'] == 'Completed':
            total_sales += float(order['total'])
            order_ids.add(order['order_id'])
            total_items_sold += int(order['quantity'])
    total_orders = len(order_ids)
    return {
        'date': date,
        'total_sales': total_sales,
        'total_orders': total_orders,
        'total_items_sold': total_items_sold
    }

def monthly_sales_summary(file_path, month, year):
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12.")

    if not isinstance(year, int) or year < 1:
        raise ValueError("Year must be a positive integer.")
    orders = read_orders_from_csv(file_path)
    total_sales = 0
    total_items_sold = 0
    order_ids = set()

    for order in orders:
        order_date = datetime.strptime(order['date'], '%Y-%m-%d')
        if order_date.month == month and order_date.year == year and order['status'] == 'Completed':
            total_sales += float(order['total'])
            order_ids.add(order['order_id'])
            total_items_sold += int(order['quantity'])
    total_orders = len(order_ids)
    return {
        'month': month,
        'year': year,
        'total_sales': total_sales,
        'total_orders': total_orders,
        'total_items_sold': total_items_sold
    }