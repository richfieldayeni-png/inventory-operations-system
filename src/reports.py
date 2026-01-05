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

from db import get_connection

def daily_delivery_report(report_date):
    """
    Returns delivery performance and cost summary per driver for a given date
    """
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT
            d.name AS driver_name,
            COUNT(DISTINCT del.delivery_id) AS total_deliveries,
            SUM(di.quantity) AS total_units_delivered,
            IFNULL(SUM(e.amount), 0) AS total_expenses
        FROM deliveries del
        JOIN drivers d ON del.driver_id = d.driver_id
        LEFT JOIN delivery_items di ON del.delivery_id = di.delivery_id
        LEFT JOIN expenses e
            ON d.driver_id = e.driver_id
            AND e.expense_date = %s
        WHERE del.delivery_date = %s
        GROUP BY d.name
        ORDER BY total_units_delivered DESC;
    """

    cursor.execute(query, (report_date, report_date))
    results = cursor.fetchall()
    conn.close()
    return results
