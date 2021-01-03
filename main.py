import cv2 
import numpy as np
import keras 

webcam_capture = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

while webcam_capture.isOpened():
    ret, frame = webcam_capture.read()
    if ret == True: 
        fgmask = fgbg.apply(frame)

        cv2.imshow("fgbg", fgmask)
        cv2.imshow("frame", frame)

        key = cv2.waitKey(0) & 0xFF

        if key == ord('q'):
            break

webcam_capture.release()
cv2.destroyAllWindows()