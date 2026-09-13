# 🔥 FireWatch AI

### AI-Powered Fire & Smoke Detection System

FireWatch AI is a computer vision-based fire and smoke detection system built using **YOLOv8**. The application analyzes uploaded images and detects the presence of fire and smoke, providing visual detection results and hazard alerts through an interactive **Streamlit** interface.

## 🔍 Overview

Early detection of fire and smoke can help improve safety and support faster response to potential hazards. FireWatch AI uses a custom-trained YOLOv8 object detection model to identify **Fire** and **Smoke** in images.

The system provides an easy-to-use interface where users can upload an image and receive AI-powered detection results.

## ✨ Features

* 🔥 Detects fire in uploaded images
* 💨 Detects smoke in uploaded images
* 🤖 Custom-trained YOLOv8 model
* 📦 Displays bounding boxes around detected objects
* 🚨 Generates hazard alerts
* 🖥️ Interactive Streamlit web interface

## 🧠 Model

* **Model:** YOLOv8 Nano
* **Framework:** Ultralytics
* **Classes:** Fire, Smoke
* **Training:** Custom fire and smoke dataset

## 🛠️ Tech Stack

* Python
* YOLOv8
* Ultralytics
* Streamlit
* OpenCV
* Pillow

## 📁 Project Structure

```text
FireWatch-AI/
│
├── app.py
├── train.py
└── README.md
```

## 🚀 Run Locally

Clone the repository and install the required dependencies:

```bash
pip install ultralytics streamlit pillow opencv-python
```

Then run:

```bash
streamlit run app.py
```

## 🎯 Applications

* Fire safety monitoring
* Early hazard detection
* Surveillance systems
* Smart buildings
* Industrial safety monitoring

## 👩‍💻 Author

Built as a Computer Vision and Deep Learning project using YOLOv8.
