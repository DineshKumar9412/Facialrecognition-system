XML LINK = Face-Detection-in-Python-using-OpenCV/data/haarcascades at master · parulnith/Face-Detection-in-Python-using-OpenCV 

Face Detection using opencv with image


import cv2
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread("girls.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
count_faces=str(len(faces))
print("number of face(s)= " + count_faces)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
cv2.imshow(" Result ", img)
cv2.imshow(" Name ", img)
cv2.waitKey(0)
Face Detection using web camera single & Multi


import cv2
import numpy as np
faceDetector = cv2.CascadeClassifier("face.xml")
cap = cv2.VideoCapture(0)
while(True):
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(gray, 1.2, 5)
    for(x, y, w, h) in faces:
      cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
    print (len(faces))
    cv2.imshow("Face", frame)
    if(cv2.waitKey(1)== ord('c')):
      break
cap.release()
cv2.destroyAllWindows()
HOW TO DRAW A RECTANGLE  IN IMAGE & PUT TEXT IN TO THE IMAGE 


for f, j in zip(s, h):
        a = (f[0:4])
        # start_point = (int(xmax), int(ymin))
        # end_point = (int(xmin), int(aymax))
        start_point = (int(a[2]), int(a[1]))
        end_point = (int(a[0]), int(a[3]))

        colors = (0, 0, 255)
        thickness = 2
        fontScale = 1
        color = (255, 255, 255)
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (100, 100)
        image = cv2.rectangle(image, start_point, end_point, colors, thickness)

        image = cv2.putText(image, j, (int(a[0]), int(a[1])), font,
                            fontScale, color, thickness, cv2.FILLED)

        # image = cv2.putText(image, j, (int(a[0]), int(a[1])),  cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255),
        #                thickness=2)

cv2.imshow("Test", image)
cv2.waitKey(0)
cv2.destroyWindow()
 

YOLOV5 MODEL DETECTION FINAL


import cv2
import torch
from PIL import Image
import glob
import matplotlib.pyplot as plt

model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5s.pt')  # custom model
CUDA_VISIBLE_DEVICES = "0"

model.conf = 0.25  # confidence threshold (0-1)
model.iou = 0.45  # NMS IoU threshold (0-1)

# dataset_name = 'zi'
test_img_path = 'glass542bd9f8abee12cb4803c40006e3c01b.jpg'
image = cv2.imread(test_img_path)

test_imgs = sorted(glob.glob(test_img_path))
print(len(test_imgs))

for img in test_imgs:
    img2 = cv2.imread(img)[:, :, ::-1]
    imgs = [img2]
    # print(img2)
    results = model(imgs, size=640)
    results.print()
    # print(results.xyxy[0])
    print(results.pandas().xyxy[0])
    a = results.pandas().xyxy[0]
    name = a['name']

    # s = list(a)
    s = a.values.tolist()
    h = name.values.tolist()

    for f, j in zip(s, h):
        a = (f[0:4])
        # start_point = (int(xmax), int(ymin))
        # end_point = (int(xmin), int(aymax))
        start_point = (int(a[2]), int(a[1]))
        end_point = (int(a[0]), int(a[3]))

        colors = (0, 0, 255)
        thickness = 2
        fontScale = 1
        color = (255, 255, 255)
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (100, 100)
        image = cv2.rectangle(image, start_point, end_point, colors, thickness)

        image = cv2.putText(image, j, (int(a[0]), int(a[1])), font,
                            fontScale, color, thickness, cv2.FILLED)

        # image = cv2.putText(image, j, (int(a[0]), int(a[1])),  cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255),
        #                thickness=2)

cv2.imshow("Test", image)
cv2.waitKey(0)
cv2.destroyWindow()
