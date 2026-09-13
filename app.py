import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

# Page configuration
st.set_page_config(
    page_title="FireWatch AI",
    page_icon="🔥",
    layout="wide"
)

# Load the trained model
@st.cache_resource
def load_model():
    return YOLO("runs/detect/firewatch_project/fire_smoke_model-2/weights/best.pt")


model = load_model()


# Header
st.title("🔥 FireWatch AI")
st.subheader("AI-Powered Fire & Smoke Detection System")

st.write(
    "Upload an image and let our AI detect potential fire and smoke hazards."
)

st.divider()


# Upload image
uploaded_file = st.file_uploader(
    "📤 Upload an image",
    type=["jpg", "jpeg", "png"]
)


if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    col1, col2 = st.columns(2)

    # Show original image
    with col1:
        st.subheader("📷 Original Image")
        st.image(image, use_container_width=True)

    # Detect button
    if st.button("🔥 Analyze Image", use_container_width=True):

        with st.spinner("🤖 FireWatch AI is analyzing the image..."):

            results = model(image)

            # Create annotated image
            annotated_image = results[0].plot()

            # Convert BGR to RGB
            annotated_image = annotated_image[:, :, ::-1]

        # Show results
        with col2:
            st.subheader("🔍 Detection Results")
            st.image(annotated_image, use_container_width=True)

        # Check detections
        detected_classes = []

        for box in results[0].boxes:

            class_id = int(box.cls[0])
            class_name = model.names[class_id]

            detected_classes.append(class_name)

        st.divider()

        # Alerts
        if "Fire" in detected_classes:
            st.error("🚨 FIRE DETECTED! Immediate attention may be required.")

        if "Smoke" in detected_classes:
            st.warning("⚠️ SMOKE DETECTED! Please investigate the area.")

        if not detected_classes:
            st.success("✅ No fire or smoke detected.")

        # Detection summary
        st.subheader("📊 Detection Summary")

        st.write(f"**Objects Detected:** {len(detected_classes)}")

        if detected_classes:
            st.write(
                "**Detected:** " + ", ".join(set(detected_classes))
            )