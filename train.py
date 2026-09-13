from ultralytics import YOLO

# Load the pre-trained YOLOv8 Nano model
model = YOLO("yolov8n.pt")

# Train the model
model.train(
    data="fire-smoke-dataset/data.yaml",
    epochs=20,
    imgsz=640,
    batch=8,
    project="firewatch_project",
    name="fire_smoke_model"
)