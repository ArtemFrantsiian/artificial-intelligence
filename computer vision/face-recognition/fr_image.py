import cv2 as cv
from pathlib import Path

path_to_folder = Path(__file__).parent.resolve()

image = cv.imread(str(path_to_folder / "static/example.jpg"))
faceCascade = cv.CascadeClassifier(str(path_to_folder / "models/haarcascade_frontalface_alt.xml"))

# Our operations on the frame come here
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.2,
    minNeighbors=5,
    minSize=(30, 30)
)

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 2)

# Display the resulting frame
cv.imshow('image', image)
cv.waitKey(0)
