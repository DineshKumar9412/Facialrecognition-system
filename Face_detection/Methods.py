1.Using MTCNN created the bounding box for the frame captured by webcam.

import cv2
from mtcnn.mtcnn import MTCNN
import os
import time
detector = MTCNN()
vid = cv2.VideoCapture(0)
while (True): 
    ret, frame = vid.read()
    result = detector.detect_faces(frame)
    # print(result)
    bounding_box = result[0]['box']
    keypoints = result[0]['keypoints']
    print(bounding_box)
    if cv2.waitKey(1) & 0xFF == 'q' :
          break
vid.release()
cv2.destroyAllWindows()print(bounding_box)
2. Using haar_cascade-frontalface.xml  created the bounding box for the frame captured by webcam

import cv2
classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
vid = cv2.VideoCapture(0)
while (True):
    ret, frame = vid.read()
    bboxes = classifier.detectMultiScale(frame)
    print(bboxes)
    if cv2.waitKey(1) & 0xFF == 'q':
        break

vid.release()
cv2.destroyAllWindows()
haarcascade_frontalface_default.xml
27 Jul 2021, 01:09 PM
3. Using dnn  created the bounding box for the frame captured by webcam.

from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import time
import cv2
proto = "models/deploy.prototxt"
model = "models/Widerface-RetinaFace.caffemodel"
net = cv2.dnn.readNetFromCaffe(proto , model)
vid = cv2.VideoCapture(0)

while True:
   
    ret,frame = vid.read()
    frame = imutils.resize(frame, width=400)

    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,
                                 (300, 300), (104.0, 177.0, 123.0))

    net.setInput(blob)
    detections = net.forward()

    for i in range(0, detections.shape[2]):  
        confidence = detections[0, 0, i, 2]
        if confidence < 0.5:
            continue
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")
        boundingbox = [startX, startY, endX, endY]
        print(boundingbox) 
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

# do a bit of cleanup
vid.release()
cv2.destroyAllWindows()

res10_300x300_ssd_iter_140000.caffemodel
27 Jul 2021, 01:26 PM

deploy.prototxt.txt
27 Jul 2021, 01:25 PM
 

HOW TO GET 5TH Frame in cv2

import cv2

test = "test/"
cap = cv2.VideoCapture(0)

count = 1
while cap.isOpened():
    ret, frame = cap.read()
    if count % 5 == 0:
        
        cv2.imshow('Frame',frame)
        cv2.imwrite("{}/img{}.jpg".format(test, count), bounding_box)
    if cv2.waitKey(1) == 13 or count == 15:
        break
    count += 1

cap.release()
cv2.destroyAllWindows()
 

Face Crop and save

import cv2
from mtcnn.mtcnn import MTCNN

detector = MTCNN()
img = cv2.imread("1636626913878.JPEG")
result = detector.detect_faces(img)
bounding_box = result[0]['box']


x1, y1, width, height = bounding_box
x2, y2 = x1 + width, y1 + height

face_boundary = img[y1:y2, x1:x2]

# img = cv2.imwrite("gfgf.jpg", face_boundary)
img = cv2.cvtColor(face_boundary, cv2.COLOR_BGR2RGB)
img = cv2.resize(img, (112, 112))

cv2.imwrite("gfgf.jpg", img)
