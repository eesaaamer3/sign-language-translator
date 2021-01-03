import cv2 
import os 
import numpy as np
import glob
import keras 
import argparse

# Temporary code from OpenCV documentation - Delete after 
parser = argparse.ArgumentParser(description='This program shows how to use background subtraction methods provided by \
                                              OpenCV. You can process both videos and images.')
parser.add_argument('--input', type=str, help='Path to a video or a sequence of image.', default='vtest.avi')
parser.add_argument('--algo', type=str, help='Background subtraction method (KNN, MOG2).', default='MOG2')
args = parser.parse_args()

# create the Background Subtractor Objects 
if args.algo == "MOG2":
    backSub = cv2.createBackgroundSubtractorMOG2()
else:
    backSub = cv2.createBackgroundSubtractorKNN()

webcam_capture = cv2.VideoCapture(cv2.samples.findFileorKeep(args.input))
if not webcam_capture.isOpened:
    print("Unable to open: " + args.input)

while True:
    ret, frame = webcam_capture.read()
    if frame is None:
        break