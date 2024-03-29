import cv2 as cv

img = cv.imread('computer-science-booth.jpg')
face_model = cv.CascadeClassifier('face-detect-model.xml')
gray_scal = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faces = face_model.detectMultiScale(gray_scal)

for (x,y,w,h) in faces:
    cv.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2) #RGB -> BGR


cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
