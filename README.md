Ethical AI Surveillance System – Face Anonymization

Objective
To demonstrate how AI-based surveillance systems operate and highlight ethical concerns such as privacy invasion and data misuse.  
This project provides an **ethical solution** by applying **face anonymization (blurring)** to protect individual identities.

---
Algorithm
1. Start the program.  
2. Import necessary libraries (`OpenCV`).  
3. Load an image or video frame containing human faces.  
4. Detect faces using a **Haar Cascade Classifier**.  
5. Apply **Gaussian Blur** to anonymize detected faces.  
6. Display the original and blurred images for comparison.  
7. End the program.

---

 Code Overview
```python
import cv2

# Load face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Read image
image = cv2.imread("people.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Blur faces
for (x, y, w, h) in faces:
    face_region = image[y:y+h, x:x+w]
    blurred_face = cv2.GaussianBlur(face_region, (99, 99), 30)
    image[y:y+h, x:x+w] = blurred_face

cv2.imshow("Ethical Surveillance Output", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
