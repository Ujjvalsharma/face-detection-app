# Face Detection App

This is a simple Face Detection Python application using OpenCV.  
The app captures a face from webcam and saves the image with the person's name and current date-time.

## 📂 Project Structure
Face_Detection_App/
├── captured_faces/ # Folder where captured faces are saved
├── haarcascade_frontalface_default.xml # Haarcascade face detection model
├── face_detect.py # Main Python file
├── requirements.txt # Required Python libraries
└── README.md # Project documentation


## ⚙️ How It Works

1. The script opens your webcam.
2. Asks the name of the person.
3. Captures face frames using OpenCV.
4. Saves the captured face images into a folder named after the person.

## 🚀 Getting Started

### 🔧 Install Required Libraries

Use pip to install required packages:

```bash
pip install -r requirements.txt

python face_detect.py
Then follow the on-screen prompt to enter the person's name. The camera will start and begin capturing.
🖼️ Output
Captured images will be stored in a folder named after the user inside captured_faces/.

Each image will be timestamped (if added later).
