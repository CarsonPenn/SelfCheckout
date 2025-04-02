# pip install mysql-connector-python
import mysql.connector

def insert_detection_data(transaction_id, detections, image_path):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Dragonsrule1",
        database="selfcheckout"
    )
    cursor = conn.cursor()

    # Insert transaction
    cursor.execute(
        "INSERT INTO transactions (transaction_id, image_path) VALUES (%s, %s)",
        (transaction_id, image_path)
    )

    # Insert detections
    for det in detections:
        cursor.execute("""
            INSERT INTO detections (transaction_id, label, confidence, x_min, y_min, x_max, y_max)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            transaction_id,
            det['label'],
            det['confidence'],
            det['x_min'],
            det['y_min'],
            det['x_max'],
            det['y_max']
        ))

    conn.commit()
    cursor.close()
    conn.close()
    print(f"✅ Inserted {len(detections)} detections for {transaction_id}")


def insert_receipt(transaction_id, items):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Dragonsrule1",
        database="selfcheckout"
    )
    cursor = conn.cursor()

    query = """
        INSERT INTO receipt_items (transaction_id, label)
        VALUES (%s, %s)
    """
    # Insert the values from the scan
    # Would change this to use scanned items
    values = [(transaction_id, item['label']) for item in items]

    # Insert custom items
    # Use this to test discrepancies
    values = [(transaction_id, item) for item in ["orange", "orange", "banana", "corn", "olive", "beans", "apple", "potato", "potato"]] # change list to whatever items you want 

    cursor.executemany(query, values)
    conn.commit()
    cursor.close()
    conn.close()

def insert_discrepancy(transaction_id, issue, resolved=False):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Dragonsrule1",
        database="selfcheckout"
    )
    cursor = conn.cursor()

    query = """
        INSERT INTO discrepancies (transaction_id, issue, resolved)
        VALUES (%s, %s, %s)
    """
    cursor.execute(query, (transaction_id, issue, resolved))
    conn.commit()
    cursor.close()
    conn.close()


def get_all_transaction_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Dragonsrule1",
        database="selfcheckout"
    )
    cursor = conn.cursor(dictionary=True)  # fetch as dicts for easy handling

    # Get all transactions
    cursor.execute("SELECT * FROM transactions ORDER BY timestamp DESC")
    transactions = cursor.fetchall()

    for txn in transactions:
        txn_id = txn['transaction_id']

        # Get detections
        cursor.execute("SELECT * FROM detections WHERE transaction_id = %s", (txn_id,))
        txn['detections'] = cursor.fetchall()

        # Get receipt items
        cursor.execute("SELECT * FROM receipt_items WHERE transaction_id = %s", (txn_id,))
        txn['receipt_items'] = cursor.fetchall()

        # Get discrepancies
        cursor.execute("SELECT * FROM discrepancies WHERE transaction_id = %s", (txn_id,))
        txn['discrepancies'] = cursor.fetchall()

    cursor.close()
    conn.close()
    return transactions

def get_receipt(transaction_id):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Dragonsrule1",
        database="selfcheckout"
    )
    cursor = conn.cursor()

    query = """
        SELECT label FROM receipt_items
        WHERE transaction_id = %s
    """
    cursor.execute(query, (transaction_id,))
    results = [row[0] for row in cursor.fetchall()]

    cursor.close()
    conn.close()

    return results

