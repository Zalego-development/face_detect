# Guide to the opencv code:
# https://towardsdatascience.com/a-guide-to-face-detection-in-python-3eab0f6b9fc1
# https://realpython.com/face-recognition-with-python/


import os
#os.environ['OPENCV_IO_MAX_IMAGE_PIXELS']=str(2**64)
import cv2
import sys
from pathlib import Path

#Locate the pretained weights from the opencvFaces
cascPath = "/Users/macbook0/Desktop/opencv_faces/venv/lib/python3.9/site-packages/cv2/data/haarcascade_frontalface_default.xml"
eyePath = "/Users/macbook0/Desktop/opencv_faces/venv/lib/python3.9/site-packages/cv2/data/haarcascade_eye.xml"

#Remember, the cascade is just an XML file that contains the data to detect faces.
#Declare cascade classifiers
faceCascade = cv2.CascadeClassifier(cascPath)
eyeCascade = cv2.CascadeClassifier(eyePath)

for file_name in os.listdir("/Users/macbook0/Desktop/opencv_faces/face401/"):
    if file_name.split(".")[-1].lower() in {"jpeg", "jpg", "png"}:
        img = cv2.imread("/Users/macbook0/Desktop/opencv_faces/face401/" + file_name, 0)


        # Read the image
        #image = cv2.imread('5.png', 0)
        #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        #The detectMultiScale function is a general function that detects objects. Since we are calling it on the face cascade, that’s what it detects.
        # The second is the scaleFactor. Since some faces may be closer to the camera, they would appear bigger than the faces in the back. The scale factor compensates for this.
        #The detection algorithm uses a moving window to detect objects. minNeighbors defines how many objects are detected near the current one before it declares the face found. minSize, meanwhile, gives the size of each window.
        # scaleFactor : Parameter specifying how much the image size is reduced at each image scale.
        # Detect faces in the image
        faces = faceCascade.detectMultiScale(
            img,
            scaleFactor=1.45,
            minNeighbors=5,
            minSize=(30, 30),
            flags = cv2.CASCADE_SCALE_IMAGE
        )
        #print(faces)

        if len(faces) >= 1:
            with open ("face_file.txt", "a") as f:
                f.write(f"{file_name}\n")
            f.close()


        if len(faces) == 0:
            with open ("no_face_file.txt", "a") as f:
                f.write(f"{file_name}\n")
            f.close()
            #print(file_name)
            os.remove(os.path.abspath("face401/" + file_name))

        print("Found {0} faces!".format(len(faces)))

        # Draw a rectangle around the faces
        # for (x, y, w, h) in faces:
        #     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # cv2.imshow("Faces found", img)
        # cv2.waitKey(10)

