
from ultralytics import YOLO
import os
import numpy as np
import cv2 as cv



def train():
    # Path to the YOLO configuration file for classification
    model = YOLO("yolov8n-cls.pt")
    
    # Path to your dataset
    data_path = '/Users/derickshi/Documents/Yolomedical/data'
    
    save_dir = '/Users/derickshi/Documents/Yolomedical/runs/muscleclassify'

    # Train the model
    results = model.train(data=data_path, epochs=2, project = save_dir)


def predict(img, st):
    # Path to the best weights file after training
    model_path = os.path.join('.', 'runs', 'muscleclassify', 'train17', 'weights', 'best.pt')
    #model_path = '/Users/derickshi/Documents/Yolomedical/bonebest.pt'
    # Load the trained model
    model = YOLO(model_path)
    
    # Predict the class of the input image
    results = model.predict(img)
    result = results[0]
    
    # Get class names and probabilities
    class_names = result.names
    probs = result.probs.data.tolist()
    class_name = class_names[np.argmax(probs)].upper()
    
    # Display the class name on the image
    height, width = img.shape[:2]
    cv.putText(img, class_name, (width - 200, 60), cv.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3, cv.LINE_AA)
    
    # Display the image using Streamlit
    st.subheader('Output Image')
    st.image(img, channels="BGR", use_column_width=True)




