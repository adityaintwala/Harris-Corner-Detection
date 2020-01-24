# -*- coding: utf-8 -*-
"""
Aditya Intwala

This is a script to demonstrate the implementation of Harris corner function to
detect corners from the image.

The script was provided to the students of ACM Winter School December 2019 held
at IISER Pune, for introducing them on the topic of feature detection from images.

"""

import argparse
import cv2
import numpy as np

def find_harris_corners(input_img, k, window_size, threshold):
    
    corner_list = []
    output_img = cv2.cvtColor(input_img.copy(), cv2.COLOR_GRAY2RGB)
    
    offset = int(window_size/2)
    y_range = input_img.shape[0] - offset
    x_range = input_img.shape[1] - offset
    
    
    dy, dx = np.gradient(input_img)
    Ixx = dx**2
    Ixy = dy*dx
    Iyy = dy**2
    
    
    for y in range(offset, y_range):
        for x in range(offset, x_range):
            
            #Values of sliding window
            start_y = y - offset
            end_y = y + offset + 1
            start_x = x - offset
            end_x = x + offset + 1
            
            #The variable names are representative to 
            #the variable of the Harris corner equation
            windowIxx = Ixx[start_y : end_y, start_x : end_x]
            windowIxy = Ixy[start_y : end_y, start_x : end_x]
            windowIyy = Iyy[start_y : end_y, start_x : end_x]
            
            #Sum of squares of intensities of partial derevatives 
            Sxx = windowIxx.sum()
            Sxy = windowIxy.sum()
            Syy = windowIyy.sum()

            #Calculate determinant and trace of the matrix
            det = (Sxx * Syy) - (Sxy**2)
            trace = Sxx + Syy
            
            #Calculate r for Harris Corner equation
            r = det - k*(trace**2)

            if r > threshold:
                corner_list.append([x, y, r])
                output_img[y,x] = (0,0,255)
    
    return corner_list, output_img 

def main():
    
    parser = argparse.ArgumentParser(description='Find Harris cornes from the image.')
    parser.add_argument('image_path', type=str, help='Full path of the input image.')
    parser.add_argument('--k', type=float, help='Value of Harris corner constant between 0.04 - 0.06.')
    parser.add_argument('--window_size', type=int, help='Size / length of the windowing function / sliding window.')
    parser.add_argument('--threshold', type=float, help='Threshold value to consider corner for particular response value.')
    
    args = parser.parse_args()
    
    img_path = args.image_path
    k = 0.04
    window_size = 5
    threshold = 10000.00
    
    if args.k:
        k = args.k
    
    if args.window_size:
        window_size = args.window_size
        
    if args.threshold:
        threshold = args.threshold
        
    input_img = cv2.imread(img_path, 0)
    
    cv2.imshow('Input Image', input_img)
    cv2.waitKey(0)

    if input_img is not None:
        
        print ("Detecting Corners Started!")
        corner_list, corner_img = find_harris_corners(input_img, k, window_size, threshold)
        
        cv2.imshow('Detected Corners', corner_img)
        cv2.waitKey(0)
        
        corner_file = open('corners_list.txt', 'w')
        corner_file.write('x ,\t y, \t r \n')
        for i in range(len(corner_list)):
            corner_file.write(str(corner_list[i][0]) + ' , ' + str(corner_list[i][1]) + ' , ' + str(corner_list[i][2]) + '\n')
        corner_file.close()
        
        if corner_img is not None:
            cv2.imwrite("corners_img.png", corner_img)
    else:
        print ("Error in input image!")
            
    print ("Detecting Corners Complete!")



if __name__ == "__main__":
    main()
