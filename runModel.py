from ultralytics import YOLO
import cv2
import uuid
from pathlib import Path
from db_utils import *

def runModel(model_path='my_model2.pt', source='0', show=True, save=True):
    """
    Runs the yolo model, etheir from the webcam or a file we provide in "source"

    Args:
        model_path (str): Path to the YOLO model file (.pt).
        source (str or int): Source of the input. 0 for webcam, or a file path for an image/video.
        show (bool): Whether to display the predictions in a pop-up window.
        save (bool): Whether to save the predictions to the runs/detect folder.
    """

    # Load the YOLO model
    model = YOLO(model_path)
    transaction_id = str(uuid.uuid4())[:8]

    results = model.predict(
        source=source,
        show=show,
        save=save,
        project='outputs',
        name=transaction_id
    )


    all_detections = []
    for r in results:
        names = r.names
        image_path = None
        if save and r.save_dir:
            image_path = Path(r.save_dir) / Path(r.path).name

        for box in r.boxes:
            class_id = int(box.cls[0])
            label = names[class_id]
            confidence = float(box.conf[0])
            x_min, y_min, x_max, y_max = map(int, box.xyxy[0])

            all_detections.append({
                "label": label,
                "confidence": confidence,
                "x_min": x_min,
                "y_min": y_min,
                "x_max": x_max,
                "y_max": y_max
            })

    insert_detection_data(transaction_id, all_detections, str(image_path) if image_path else None)
    insert_receipt(transaction_id, all_detections) # This is just for convience. This would later be changed to get information from the actually scanned items

    detected_labels = set(d["label"] for d in all_detections)
    receipt_labels = set(get_receipt(transaction_id))

    # Find mismatches
    extra_in_detected = detected_labels - receipt_labels
    extra_in_receipt = receipt_labels - detected_labels

    for label in extra_in_detected:
        insert_discrepancy(transaction_id, f"Detected '{label}' not in receipt")

    for label in extra_in_receipt:
        insert_discrepancy(transaction_id, f"Receipt item '{label}' not detected by YOLO")


    print("✅ YOLO prediction and DB insert complete.")

# Example usage
if __name__ == "__main__":
    runModel(source='test_files/group1.jpg')  # Or 0 for webcam
