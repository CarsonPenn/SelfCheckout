import mysql.connector

def insert_receipt(transaction_id, items):
    """
    Inserts a list of items into the receipt_items table for the given transaction_id.

    Args:
        transaction_id (str): The unique ID of the transaction.
        items (list[str]): A list of item labels to insert.
    """
    conn = mysql.connector.connect(
        host='localhost',
        user='your_username',
        password='your_password',
        database='selfcheckout'
    )
    cursor = conn.cursor()

    query = """
        INSERT INTO receipt_items (transaction_id, label)
        VALUES (%s, %s)
    """
    values = [(transaction_id, item) for item in items]

    cursor.executemany(query, values)
    conn.commit()
    cursor.close()
    conn.close()
