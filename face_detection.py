import cv2
import numpy as np
import os


def face():
    fa = cv2.CascadeClassifier('faces.xml')  # load face features
    # cap=cv2.VideoCapture('sample.mp4')
    cap = cv2.VideoCapture(0)  # capture from video
    ret = True
    while ret:  # find face and draw rectangle box
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = fa.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cropped = frame[y:y + h, x:x + w]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)

        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    return
