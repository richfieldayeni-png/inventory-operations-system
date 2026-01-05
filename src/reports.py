from db import get_connection

def inventory_report():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.name, i.quantity
        FROM inventory i
        JOIN products p ON i.product_id = p.product_id
    """)
    results = cursor.fetchall()
    conn.close()
    return results
