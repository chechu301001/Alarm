import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# WEBCAM 
cap = cv2.VideoCapture(0)

while True:
    # READ FRAME
    _, img = cap.read()

    # CONVERT TO GRAYSCALE
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # DETECT
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # RECTANGLE
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # SHOW
    cv2.imshow('img', img)

    # ESCAPE KEY TO STOP
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
        
# RELEASE
cap.release()