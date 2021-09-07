import cv2
import numpy as np

frame = cv2.imread('..\Photos/lane_img.jpg')
edges = cv2.Canny(frame,100,200) # This uses the canny edge detector. The 100 and 200 are rather arbitrary parameters; the second should be larger than the first, play around to see what numbers work best for each image.


# Use the Canny again.

minLineLength=1000
maxLineGap=10
edges = cv2.Canny(frame,100,200)
lines = cv2.HoughLinesP(edges,1,np.pi/180,150,minLineLength,maxLineGap)
'''
https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html
https://learnopencv.com/hough-transform-with-opencv-c-python/
'''

blankImage = np.zeros(frame.shape)

#draw the lines onto our blank image
for l in lines:
    for x1,y1,x2,y2 in l:
        cv2.line(blankImage,(x1,y1),(x2,y2),(0,255,0),5)


cv2.imshow("original", frame)
cv2.imshow("road_lines", blankImage)
cv2.waitKey(-1)