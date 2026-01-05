from db import get_connection

def add_driver(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO drivers (name) VALUES (%s)",
        (name,)
    )
    conn.commit()
    conn.close()

def create_delivery(driver_id, delivery_date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO deliveries (driver_id, delivery_date) VALUES (%s, %s)",
        (driver_id, delivery_date)
    )
    conn.commit()
    conn.close()

def add_delivery_item(delivery_id, product_id, quantity):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO delivery_items (delivery_id, product_id, quantity)
        VALUES (%s, %s, %s)
        """,
        (delivery_id, product_id, quantity)
    )
    conn.commit()
    conn.close()

def log_expense(driver_id, amount, expense_date, description):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO expenses (driver_id, amount, expense_date, description)
        VALUES (%s, %s, %s, %s)
        """,
        (driver_id, amount, expense_date, description)
    )
    conn.commit()
    conn.close()
