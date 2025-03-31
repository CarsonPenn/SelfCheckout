from ultralytics import YOLO
import cv2
import time

def runModel(model_path='my_model2.pt', source='0', show=True, save=True, save_video=True, save_list=True):
    """
    Runs the YOLO model, either from the webcam or a file we provide in "source".
    Also optionally saves a video and a list of detected objects.

    Args:
        model_path (str): Path to the YOLO model file (.pt).
        source (str or int): Source of the input. 0 for webcam, or a file path for an image/video.
        show (bool): Whether to display the predictions in a pop-up window.
        save (bool): Whether to save the predictions to the runs/detect folder.
        save_video (bool): Whether to save the processed video to a file.
        save_list (bool): Whether to save a list of detected objects to a text file.
    """

    # Load the YOLO model
    model = YOLO(model_path)
    detected_objects = []  # List to store detected objects

    # If using webcam
    if source == '0' or source == 0:
        cap = cv2.VideoCapture(0)  # Open the webcam
        if save_video:
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter('output.avi', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))
            
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            results = model.predict(source=frame, show=show, save=False)

            for result in results:
                for det in result.boxes.data.tolist():
                    x1, y1, x2, y2, conf, cls = det
                    class_name = model.names[int(cls)]
                    detected_objects.append(class_name)

            if save_video:
                out.write(frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        if save_video:
            out.release()
        cv2.destroyAllWindows()

    # If using a file
    else:
        results = model.predict(source=source, show=show, save=save)
        for result in results:
            for det in result.boxes.data.tolist():
                x1, y1, x2, y2, conf, cls = det
                class_name = model.names[int(cls)]
                detected_objects.append(class_name)

    print("Prediction complete!")

    # Save the list of detected objects
    if save_list:
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        with open(f"detected_objects_{timestamp}.txt", "w") as f:
            for obj in detected_objects:
                f.write(obj + "\n")
        print(f"Detected objects list saved to detected_objects_{timestamp}.txt")

# Example usage:
runModel(source='0', save_video=True, save_list=True) #saves the video and the list.
#runModel(source="test_files/3bb65d7b-IMG_8343.jpg") #example for image input, this will not save a video.