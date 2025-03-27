# You must be in the aconda environment to run the code.
from ultralytics import YOLO
import cv2

# Load the YOLO model
model = YOLO('my_model2.pt')  

# Choose the source: 0 for webcam, or a file path for an image/video
# You will get a breif pop up then the image or video will be saved in the runs/detect folder.
# source = '0'
source = 'test_files/3bb65d7b-IMG_8343.jpg'

# Run YOLO predictions
results = model.predict(source=source, show=True, save=True)

# If using a webcam, keep it open until 'q' is pressed
# When you run the webcam you don't see a pop up yet, it will have the output in the terminal. 
# You will find the video in the runs/detect folder.
if source == 0:
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

print("Prediction complete!")