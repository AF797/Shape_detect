import os
import math
import cv2

def setLabel(img, pts, label):
    (x, y, w, h) = cv2.boundingRect(pts)
    pt1 = (x, y)
    pt2 = (x + w, y + h)
    cv2.putText(img, label, (pt1[0], pt1[1]-3), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))

img = cv2.imread('ppap.JPG')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thr = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)

contours, _ = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(img, contours, -1, (0,0,255), 4)

for cont in contours:
    approx = cv2.approxPolyDP(cont, cv2.arcLength(cont, True) * 0.02, True)
    vtc = len(approx)

    if vtc == 3:
        setLabel(img, cont, 'Triangle')
    elif vtc == 4:
        setLabel(img, cont, 'Rectangle')
    elif vtc == 5:
        setLabel(img, cont, 'Pentagon')
    elif vtc == 6:
        setLabel(img, cont, 'Hexagon')
    else:
        area = cv2.contourArea(cont)
        _, radius = cv2.minEnclosingCircle(cont)

        ratio = radius * radius * math.pi / area
        if int(ratio) == 1:
            setLabel(img, cont, 'Circle')

cv2.imshow('img', img)

cv2.waitKey()
cv2.destroyAllWindows()