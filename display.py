from db_utils import *
def display_transactions():
    all_data = get_all_transaction_data()

    for txn in all_data:
        print(f"\n🧾 Transaction ID: {txn['transaction_id']}")
        print(f"🕒 Timestamp: {txn['timestamp']}")
        print(f"🖼️ Image Path: {txn['image_path']}")

        print("\n📦 Detections:")
        for d in txn['detections']:
            print(f" - {d['label']} ({d['confidence']:.2f})")

        print("\n📝 Receipt Items:")
        for item in txn['receipt_items']:
            print(f" - {item['label']}")

        print("\n⚠️ Discrepancies:")
        for issue in txn['discrepancies']:
            if issue['resolved']:
                print(f" - {issue['issue']} (Resolved: YES)")
            else:
                print(f" - {issue['issue']} (Resolved: NO)")
