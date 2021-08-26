import cv2

# Rescaling
def rescale_frame(frame,scale=0.75):
    #works for images, video and live video
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv2.resize(frame,dimensions,interpolation =cv2.INTER_AREA)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint is None:
        rotPoint=(width//2,height//2)
    
    rotMat = cv2.getRotationMatrix2D(rotPoint,angle,scale=1.0)
    dimensions =(width,height)

    return cv2.warpAffine(img,rotMat,dimensions)

img = cv2.imread(r"C:\Users\Luke\Desktop\python_opencv_workshop_usrc\Photos\strawberry.jpg")
cv2.imshow("Original Strawberry", img)
cv2.waitKey(0)

rescaledImg = rescale_frame(img, 0.5)
cv2.imshow("Rescaled strawberry", rescaledImg)
cv2.waitKey(0)

greyImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grey Strawberry',greyImg)

blurImg = cv2.GaussianBlur(img,(9,9),cv2.BORDER_DEFAULT)
cv2.imshow('Blurred Strawberry',blurImg)

cannyImg = cv2.Canny(img,125,200)
cv2.imshow('Canny Strawberry',cannyImg)
cv2.waitKey(0)

rotatedImg = rotate(img, 45)
cv2.imshow("Rotated Strawberry", rotatedImg)
cv2.waitKey(0)

circleImg = cv2.circle(img,(int(img.shape[1]/2), int(img.shape[0]/2)),40,(255,0,0),thickness=2)
cv2.imshow("Circle strawberry", circleImg)
cv2.waitKey(0)