import cv2
import streamlit as st
from PIL import Image
import numpy as np

st.set_page_config(page_title="Face Detection App", layout="centered")

st.title("😊 Face Detection App")
st.write("Upload an image or use webcam to detect faces.")

# Load pre-trained face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Upload image
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

# Convert image and detect faces
def detect_faces(image):
    img_np = np.array(image.convert('RGB'))
    gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img_np, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return img_np, len(faces)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    result_img, face_count = detect_faces(image)
    st.image(result_img, caption=f"Detected Faces: {face_count}", use_column_width=True)
    st.success(f"Found {face_count} face(s) in the image.")

# Optional: Use webcam
st.write("Or use webcam below 👇")
if st.button("Start Camera"):
    cap = cv2.VideoCapture(0)
    stframe = st.empty()

    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Camera not found or permission denied.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        stframe.image(frame, channels="BGR")

        # Break loop if "Stop" button is pressed
        if st.button("Stop Camera"):
            break

    cap.release()
