from db import get_connection

def add_product(name, sku, unit_price):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO products (name, sku, unit_price) VALUES (%s, %s, %s)",
        (name, sku, unit_price)
    )
    conn.commit()
    conn.close()
  
