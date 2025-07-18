{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "581e6fde",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Saved 10 photos for \n"
     ]
    },
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mThe Kernel crashed while executing code in the current cell or a previous cell. \n",
      "\u001b[1;31mPlease review the code in the cell(s) to identify a possible cause of the failure. \n",
      "\u001b[1;31mClick <a href='https://aka.ms/vscodeJupyterKernelCrash'>here</a> for more info. \n",
      "\u001b[1;31mView Jupyter <a href='command:jupyter.viewOutput'>log</a> for further details."
     ]
    }
   ],
   "source": [
    "import cv2\n",
    "import os\n",
    "\n",
    "# Load Haar Cascade face detector\n",
    "face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')\n",
    "\n",
    "# Step 1: Ask for the user's name\n",
    "user_name = input(\"Enter the name of the person: \")\n",
    "\n",
    "# Step 2: Create a folder with that name\n",
    "folder_path = f\"captured_faces/{user_name}\"\n",
    "os.makedirs(folder_path, exist_ok=True)\n",
    "\n",
    "# Step 3: Start webcam\n",
    "cap = cv2.VideoCapture(0)\n",
    "\n",
    "face_count = 0  # Count number of photos captured\n",
    "\n",
    "while True:\n",
    "    ret, frame = cap.read()\n",
    "    if not ret:\n",
    "        break\n",
    "\n",
    "    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)\n",
    "\n",
    "    # Step 4: Detect faces\n",
    "    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)\n",
    "\n",
    "    for (x, y, w, h) in faces:\n",
    "        face_count += 1\n",
    "\n",
    "        # Draw rectangle around face\n",
    "        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)\n",
    "\n",
    "        # Crop the face\n",
    "        face_img = frame[y:y+h, x:x+w]\n",
    "\n",
    "        # Step 5: Save with person’s name\n",
    "        cv2.imwrite(f\"{folder_path}/{user_name}_{face_count}.jpg\", face_img)\n",
    "\n",
    "        # Optional: Limit number of photos\n",
    "        if face_count >= 10:\n",
    "            print(f\"✅ Saved 10 photos for {user_name}\")\n",
    "            cap.release()\n",
    "            cv2.destroyAllWindows()\n",
    "            exit()\n",
    "\n",
    "    # Show the frame with rectangles\n",
    "    cv2.imshow(\"Face Capture\", frame)\n",
    "\n",
    "    # Press 'q' to quit manually\n",
    "    if cv2.waitKey(1) & 0xFF == ord('q'):\n",
    "        break\n",
    "\n",
    "# Release resources\n",
    "cap.release()\n",
    "cv2.destroyAllWindows()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
