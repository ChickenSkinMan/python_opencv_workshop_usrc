import cv2
import numpy as np

# read the cropped face image
img = cv2.imread('Faces/usrc_cropped.png')

# grayscale
grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# get faces from haar cascade
haarCascade=cv2.CascadeClassifier('Lesson 3 -Faces/haar_face.xml')

# read frame image
frame = cv2.imread('Faces/imageframe.png')

facesRect = haarCascade.detectMultiScale(grey,scaleFactor=1.1,minNeighbors=5)

faceCount = 1

for (x,y,w,h) in facesRect:
    faceROI = img[y:y+h,x:x+w,:]
    picFrame = np.zeros((w+40,h+40,3))
    picFrame = cv2.copyTo(frame,None)
    picFrame = cv2.resize(picFrame,(w+40,h+40))
    picFrame[20:h+20, 20:w+20,:] = faceROI

    cv2.imwrite('Faces/usrc_faces' + str(faceCount) + '.png', picFrame)
    faceCount += 1

cv2.waitKey(-1)