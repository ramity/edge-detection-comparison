#!/usr/bin/env python

import cv2
import numpy as np
import time
import csv

with open("./stats.csv", "w") as csv_file:

    csv_writer = csv.writer(csv_file, lineterminator = "\n")

    csv_writer.writerow(["folder", "canny_time", "prewitt_time", "sobel_time", "laplacian_time"])

    for z in range(1, 41):

        original = cv2.imread("./" + str(z) + "/original.jpg")

        gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
        original_gaussian = cv2.GaussianBlur(gray,(3,3),0)

        canny_start = time.time()
        canny = cv2.Canny(original,100,200)
        canny_time = time.time() - canny_start

        kernel_x = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
        kernel_y = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])

        prewitt_start = time.time()
        prewitt_x = cv2.filter2D(original_gaussian, -1, kernel_x)
        prewitt_y = cv2.filter2D(original_gaussian, -1, kernel_y)
        prewitt = prewitt_x + prewitt_y
        prewitt_time = time.time() - prewitt_start

        sobel_start = time.time()
        sobel_x = cv2.Sobel(original_gaussian,cv2.CV_8U,1,0,ksize=5)
        sobel_y = cv2.Sobel(original_gaussian,cv2.CV_8U,0,1,ksize=5)
        sobel = sobel_x + sobel_y
        sobel_time = time.time() - sobel_start

        laplacian_start = time.time()
        laplacian = cv2.Laplacian(original,cv2.CV_64F)
        laplacian_time = time.time() - laplacian_start

        csv_writer.writerow([z, canny_time, prewitt_time, sobel_time, laplacian_time])

        cv2.imwrite("./" + str(z) + "/canny.jpg", canny)
        cv2.imwrite("./" + str(z) + "/prewitt.jpg", prewitt)
        cv2.imwrite("./" + str(z) + "/sobel.jpg", sobel)
        cv2.imwrite("./" + str(z) + "/laplacian.jpg", laplacian)
