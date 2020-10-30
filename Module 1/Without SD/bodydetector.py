import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('test1.jpg',cv2.IMREAD_COLOR)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
low_cascade = cv2.CascadeClassifier('haarcascade_lowerbody.xml')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )

faces = face_cascade.detectMultiScale(gray, 1.1 , 4)
low = low_cascade.detectMultiScale(gray, 1.1 , 3)
    
lowesty = 0
highesty = 0
count1 = 0
count2 = 0
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (12,150,100),10)
    if count1==0:
    	highesty = y
    	count1+=10
    # print(h)
    # print(y)
    if(y>highesty):
        highesty = y
for (x,y,w,h) in low:
    if count2==0:
    	lowesty = y
    	count2+=10
    # print(h)
    # print(y)
    if(y<lowesty):
        lowesty = y
    cv2.rectangle(img, (x,y), (x+w, y+h), (12,150,100),10)

print(highesty-lowesty)

oh = highesty-lowesty-200

rh = 1710
ih = 4000
f = 25
#f = 5
ss = 12.5

x = f*rh*ih
y = oh*ss

print(x/y)

print(x/(4.6*y))

cv2.namedWindow("image", cv2.WINDOW_NORMAL)

cv2.imshow('image',img)
cv2.waitKey(0) 
# cv2.destroyAllWindows()