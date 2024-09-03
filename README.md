# DISCLAIMER
This project is an app that was primarily developed by sevdaimany. This is the original github https://github.com/sevdaimany/YOLOv8-Medical-Imaging/tree/master. The vast majority of the text below and code is the same as the project mentioned except for a few minor changes that we (John, Jack, Cameron, and Derick) added to make it better equipped for the EE-24235-01 The Science and Engineering of Digital Photography taught by Professor Hoffman at the London 1 Summer Engineering Study Abroad Program 2024. I essentially just fixed several small issues with the original file and trained/developed an additional yolov8 model on some fracture xrays images to illustrate how deep learning models could assist medical professionals.

In order to fully utilize the app, it's recommended that you create an anaconda virtual environment and activate the environment.yml file provided. Due to the wide array of packages and modules needed, it is recommended that anaconda is used instead of just directly installing the requirements file. You would then clone the repositary, cd into the file, and run the app.py file by doing:

```bash
streamlit run app.py
```

The following readme text until the end is directly copied over from the orignal github as I thought it was still pretty informative:

# YOLOv8 Medical Imaging

YOLO is known for its ability to detect objects in an image in a single pass, making it a highly efficient and accurate object detection algorithm.🎯
https://github.com/ultralytics/ultralytics?tab=readme-ov-file 
The latest version of YOLO, YOLOv8, released in January 2023 by Ultralytics, has introduced several modifications that have further improved its performance.

In this project, I will focus on three major computer vision tasks that YOLOv8 can be used for: **classification**, **detection**, and **segmentation**. I will explore how YOLOv8 can be applied in the 
field of medical imaging to detect and classify various anomalies and diseases🧪💊.


## Introduction to YOLOv8
Some of the notable modifications in YOLOv8 include:

- **New Backbone Network**: YOLOv8 adopts the powerful Darknet-53 as its backbone network, enhancing feature extraction capabilities.

- **Anchor-Free Detection**: YOLOv8 employs an anchor-free detection head, which directly predicts the center of an object instead of relying on offset values from predefined anchor boxes.

- **New Loss Function**

## Tasks

In this project, I focus on three major computer vision tasks using YOLOv8, all accessible through the Streamlit web application:

1. **Classification:** Utilize the YOLOv8 model to classify medical images into three categories: COVID-19, Viral Pneumonia, and Normal, using the [COVID-19 Image 
Dataset](https://www.kaggle.com/datasets/pranavraikokte/covid19-image-dataset).

2. **Object Detection:** Employ YOLOv8 for detecting Red Blood Cells (RBC), White Blood Cells (WBC), and Platelets in blood cell images using the [RBC and WBC Blood Cells Detection 
Dataset](https://universe.roboflow.com/tfg-2nmge/yolo-yejbs).

3. **Segmentation:** Use YOLOv8 for segmenting breast ultrasound images with the [Breast Ultrasound Images Dataset](https://www.kaggle.com/datasets/aryashah2k/breast-ultrasound-images-dataset).

## Screenshots

I used Streamlit to create a user-friendly interface for easy interaction with the YOLOv8 model. Below are screenshots of each part:

### About page

![About](https://github.com/sevdaimany/YOLOv8-Medical-Imaging/blob/master/intro_screenshot.png)


### Object Detection

![Object Detection Screenshot](https://github.com/sevdaimany/YOLOv8-Medical-Imaging/blob/master/detection/detection_screenshot.png)

### Classification

![Classification Screenshot](https://github.com/sevdaimany/YOLOv8-Medical-Imaging/blob/master/classification/classification_screenshot.png)


### Segmentation

![Segmentation Screenshot](https://github.com/sevdaimany/YOLOv8-Medical-Imaging/blob/master/segmentation/segmentation_screenshot.png)

## Installation and Usage

### Installation
(Make sure to read the disclaimer above)
1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/sevdaimany/YOLOv8-Medical-Imaging.git
   ```
2. Navigate to the project directory:

   ```bash
   cd YOLOv8-Medical-Imaging
   ```
3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:

On Windows:

   ```bash
venv\Scripts\activate

   ```

On macOS and Linux:

   ```bash
source venv/bin/activate

   ```
5. Install the required dependencies from the provided requirements.txt file:


   ```bash
   pip install -r requirements.txt
   ```


## Usage
**Using the Provided Demo Images**

I've made it easy for you to get started with our project without the need to download a dataset. I've included a set of demo images in the DEMO_IMAGES directory. You can use these images to quickly see 
how our project works.

**Run the Streamlit App:**

Start the Streamlit app to see our project in action:
```bash
streamlit run app.py
```



