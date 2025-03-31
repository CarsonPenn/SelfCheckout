from ultralytics import YOLO
import cv2

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

    # Run YOLO predictions
    results = model.predict(source=source, show=show, save=save)

    # If using a webcam, keep it open until 'q' is pressed
    if source == '0' or source == 0: 
        cap = cv2.VideoCapture(0) # Open the webcam
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            results = model.predict(source=frame, show=show, save=False) 

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    print("Prediction complete!")

# Example usage:
runModel(source='0')
