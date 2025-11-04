# Ethical AI Surveillance System – Face Anonymization Demo
import cv2
# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
# Read the input image
image = cv2.imread("C:\Users\Dell\Videos\Sample Picture.PNG")
# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
# Blur the faces to ensure privacy
for (x, y, w, h) in faces:
    face_region = image[y:y+h, x:x+w]
blurred_face = cv2.GaussianBlur(face_region, (99, 99), 30)
image[y:y+h, x:x+w] = blurred_face
# Display the output
cv2.imshow("Ethical Surveillance Output", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
