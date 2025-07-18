import cv2
import os

# Load Haar Cascade face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Step 1: Ask for the user's name
user_name = input("Enter the name of the person: ")

# Step 2: Create a folder with that name
folder_path = f"captured_faces/{user_name}"
os.makedirs(folder_path, exist_ok=True)

# Step 3: Start webcam
cap = cv2.VideoCapture(0)

face_count = 0  # Count number of photos captured

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Step 4: Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        face_count += 1

        # Draw rectangle around face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Crop the face
        face_img = frame[y:y+h, x:x+w]

        # Step 5: Save with person’s name and count
        cv2.imwrite(f"{folder_path}/{user_name}_{face_count}.jpg", face_img)

        # Optional: Limit number of photos
        if face_count >= 10:
            print(f"✅ Saved 10 photos for {user_name}")
            cap.release()
            cv2.destroyAllWindows()
            exit()

    # Show the frame with rectangles
    cv2.imshow("Face Capture", frame)

    # Press 'q' to quit manually
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

