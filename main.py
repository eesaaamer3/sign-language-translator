import cv2 
import numpy as np
import keras 



webcam_capture = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = webcam_capture.read()

    fgmask = fgbg.apply(frame)

    cv2.imshow("fgmask", fgmask)
    cv2.imshow("frame", frame)

    k = cv2.waitKey(30) & 0xff
    if k ==  27:
        break

webcam_capture.release()
cv2.destroyAllWindows()

    