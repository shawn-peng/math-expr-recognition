## http://cs229.stanford.edu/proj2013/JimenezNguyen_MathFormulas_final_paper.pdf


import cv2
import numpy as np


img = cv2.imread('../formula/test.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

thresh = cv2.adaptiveThreshold(gray,255,1,1,11,2)

thresh_color = cv2.cvtColor(thresh,cv2.COLOR_GRAY2BGR)
# apply some dilation and erosion to join the gaps
thresh = cv2.dilate(thresh,None,iterations = 1)

contours,hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.rectangle(thresh_color,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('img',img)
cv2.imshow('res',thresh_color)


if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()

### For more details & feature extraction on contours, visit : http://opencvpython.blogspot.com/2012/04/contour-features.html