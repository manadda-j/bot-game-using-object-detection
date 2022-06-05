import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
from vision import Vision
from hsvfilter import HsvFilter

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def exception(input):
    pass

def manualColorSegmentation(src_bgr):
    cv.namedWindow("Controller")
    cv.createTrackbar("HUE low", "Controller", 0, 180, exception)
    cv.createTrackbar("HUE high", "Controller", 0, 180, exception)
    cv.createTrackbar("SAT low", "Controller", 0, 255, exception)
    cv.createTrackbar("SAT high", "Controller", 255, 255, exception)
    cv.createTrackbar("Value low", "Controller", 0, 255, exception)
    cv.createTrackbar("Value high", "Controller", 255, 255, exception)

    while True:
        # Get current positions from trackbars
        min_hue = cv.getTrackbarPos("HUE low", "Controller")
        max_hue = cv.getTrackbarPos("HUE high", "Controller")
        min_sat = cv.getTrackbarPos("SAT low", "Controller")
        max_sat = cv.getTrackbarPos("SAT high", "Controller")
        min_value = cv.getTrackbarPos("Value low", "Controller")
        max_value = cv.getTrackbarPos("Value high", "Controller")

        img_hsv = cv.cvtColor(src_bgr, cv.COLOR_BGR2HSV)
        lower = np.array([min_hue, min_sat, min_value])
        upper = np.array([max_hue, max_sat, max_value])
        mask = cv.inRange(img_hsv, lower, upper)
        result = cv.bitwise_and(img_hsv, img_hsv, mask=mask)
        # Convert to HSV and split each channel

        cv.imshow("Final Output", result)
        cv.imshow("Mask", mask)
        cv.imshow("Output", src_bgr)
        if cv.waitKey(1) == 27:  # ESC to exit
            break



if __name__ == '__main__':
    src_bgr = cv.imread('22.jpg')
    manualColorSegmentation(src_bgr)

    # # initialize the WindowCapture class
    # wincap = WindowCapture('Dragonica Online (EMP) |  Patch: 10.9.5.3 (Client Ver : 2.0.101) ')
    # # initialize the Vision class
    # vision_limestone = Vision('22.jpg')
    # # initialize the trackbar window
    # vision_limestone.init_control_gui()
    #
    # # limestone HSV filter
    # # hsv_filter = HsvFilter(0, 180, 129, 15, 229, 243, 143, 0, 67, 0)
    #
    # loop_time = time()

    # while (True):
    #
    #     screenshot = wincap.get_screenshot()
    #
    #     # pre-process the image
    #     # processed_image = vision_limestone.apply_hsv_filter(screenshot, hsv_filter)
    #
    #     # do object detection
    #     # rectangles = vision_limestone.find(processed_image, 0.46)
    #
    #     # draw the detection results onto the original image
    #     output_image = vision_limestone.apply_hsv_filter(screenshot)
    #
    #     # display the processed image
    #     # cv.imshow('Processed', processed_image)
    #     cv.imshow('Matches', output_image)
    #
    #     # debug the loop rate
    #     print('FPS {}'.format(1 / (time() - loop_time)))
    #     loop_time = time()
    #
    #     # press 'q' with the output window focused to exit.
    #     # waits 1 ms every loop to process key presses
    #     if cv.waitKey(1) == ord('q'):
    #         cv.destroyAllWindows()
    #         break
    #
    # print('Done.')
