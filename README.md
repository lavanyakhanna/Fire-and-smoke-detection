# 🔥 FireWatch AI

### AI-Powered Fire & Smoke Detection System

FireWatch AI is a computer vision system that uses a **custom-trained YOLOv8 object detection model** to detect **fire and smoke in images**. The project combines deep learning with an interactive Streamlit interface to provide fast visual hazard detection and automated safety alerts.

---

## 🚀 Project Overview

Traditional fire monitoring often depends on manual surveillance or sensor-based systems. **FireWatch AI explores a computer vision-based approach**, allowing images to be analyzed automatically for visible signs of fire and smoke.

Users can upload an image through the web interface, and the trained AI model identifies potential hazards by generating:

* 🔥 Fire detections
* 💨 Smoke detections
* 📦 Bounding boxes around detected regions
* 📊 Detection summaries
* 🚨 Automated hazard alerts

---

## ✨ Key Features

* 🔥 **Fire Detection** — Identifies visible fire in images
* 💨 **Smoke Detection** — Detects potential smoke regions
* 🤖 **Custom YOLOv8 Model** — Trained on a fire and smoke dataset
* 📦 **Object Localization** — Displays bounding boxes around detections
* 🚨 **Hazard Alerts** — Generates alerts based on detected objects
* 🖥️ **Interactive Web App** — Built using Streamlit
* ⚡ **Real-Time Ready Architecture** — Lightweight model suitable for fast inference

---

## 🧠 How It Works

```text
Upload Image
     ↓
FireWatch AI
     ↓
YOLOv8 Detection Model
     ↓
Fire / Smoke Classification
     ↓
Bounding Boxes + Confidence Scores
     ↓
Hazard Alert & Detection Summary
```

---

## 🛠️ Tech Stack

| Technology      | Purpose                      |
| --------------- | ---------------------------- |
| **Python**      | Core programming language    |
| **YOLOv8**      | Object detection model       |
| **Ultralytics** | Model training and inference |
| **Streamlit**   | Interactive web application  |
| **OpenCV**      | Image processing             |
| **Pillow**      | Image handling               |

---

## 📂 Project Structure

```text
FireWatch-AI/
│
├── app.py                 # Streamlit web application
├── train.py               # YOLOv8 model training script
├── README.md              # Project documentation
├── requirements.txt       # Project dependencies
└── .gitignore             # Ignored files and folders
```

---

## 🚀 Running the Project Locally

### 1️⃣ Clone the repository

```bash
git clone <your-repository-url>
cd FireWatch-AI
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit application

```bash
streamlit run app.py
```

---

# 📊 Results

The custom-trained YOLOv8 model successfully detects the following classes:

| Class    | Detection Capability             |
| -------- | -------------------------------- |
| 🔥 Fire  | Identifies visible fire regions  |
| 💨 Smoke | Identifies visible smoke regions |

The application displays:

* Original uploaded image
* AI-generated detection output
* Bounding boxes around detected hazards
* Detected object summary
* Fire and smoke safety alerts

> **Note:** Detection performance depends on image quality, lighting conditions, and how closely the input resembles the training dataset.

---

## 🎯 Potential Applications

* 🏭 Industrial safety monitoring
* 🏢 Smart building surveillance
* 🌲 Forest and wildfire monitoring
* 🏠 Residential safety systems
* 📹 CCTV-based hazard detection

---

## 🔮 Future Improvements

* 🎥 Real-time webcam detection
* 📹 CCTV/video stream support
* 🔔 Automated emergency notifications
* ☁️ Cloud deployment
* 📊 Detection analytics dashboard
* 🗺️ Location-based incident monitoring

---

## 💡 What I Learned

Through this project, I gained hands-on experience with:

* Training a custom object detection model
* Working with YOLOv8 and Ultralytics
* Preparing and using annotated datasets
* Building an AI-powered Streamlit application
* Performing computer vision inference
* Integrating machine learning models into user-facing applications

---

## 👩‍💻 Author

**Lavanya Khanna**

Built as a hands-on **Computer Vision and Deep Learning project** using YOLOv8 and Streamlit.
