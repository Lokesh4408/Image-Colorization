import cv2
import os
from math import log10, sqrt 
import numpy as np 

# Define original and colorized paths:
path_original = '/home/lokesh/Desktop/mediaSubjects/IVP/avt_image_db'
path_colorized = '/home/lokesh/Desktop/mediaSubjects/IVP/objectiveMetrics/avt_image_db_chromagan'
start_point = 0 # Define the start point for searching the image name (e.g. if the name has a prefix)
                # Supports only one method per folder

# Save PSNR for each image and color channel in an array:
psnr_blue = np.array([])
psnr_green = np.array([])
psnr_red = np.array([])

# Loop through images in the original folder:
for filename in os.listdir(path_original):
    if filename.endswith('.png') or filename.endswith('.jpg'):
        original = cv2.imread(f'{path_original}/{filename}')
        b_original, g_original, r_original = cv2.split(original) # split into BGR
        print("step0")
        
        # Find the corresponding image in the colorized folder:
        for filename_colorized in os.listdir(path_colorized):
            if filename_colorized.endswith('.png') or filename_colorized.endswith('.jpg'):
                print("step1")
                if filename_colorized.startswith(filename, start_point) or filename_colorized.startswith(filename, start_point):
                    print("step2")
                    colorized = cv2.imread(f'{path_colorized}/{filename_colorized}')
                    b_colorized, g_colorized, r_colorized = cv2.split(colorized) # split into BGR
                    print("step3")
        
        # PSNR Blue
        mse = np.mean((b_original - b_colorized) ** 2) 
        if(mse == 0):  # MSE is zero means no noise is present in the signal . 
                       # Therefore PSNR have no importance. 
            pnsr_sum = 100
        max_pixel = 255.0
        psnr_b = 20 * log10(max_pixel / sqrt(mse))
        psnr_blue = np.append(psnr_blue, psnr_b)
        
        # PSNR Green
        mse = np.mean((g_original - g_colorized) ** 2) 
        if(mse == 0):  # MSE is zero means no noise is present in the signal . 
                       # Therefore PSNR have no importance. 
            pnsr_sum = 100
        max_pixel = 255.0
        psnr_g = 20 * log10(max_pixel / sqrt(mse))
        psnr_green = np.append(psnr_green, psnr_g)
    
        # PSNR Red
        mse = np.mean((r_original - r_colorized) ** 2) 
        if(mse == 0):  # MSE is zero means no noise is present in the signal . 
                       # Therefore PSNR have no importance. 
            pnsr_sum = 100
        max_pixel = 255.0
        psnr_r = 20 * log10(max_pixel / sqrt(mse))
        psnr_red = np.append(psnr_red, psnr_b)
        
# Compute mean values:
mean_psnr_b = np.mean(psnr_blue)
mean_psnr_g = np.mean(psnr_green)
mean_psnr_r = np.mean(psnr_red)

print(f"Mean PSNR value for blue channel: {round(mean_psnr_b, 2)} dB")
print(f"Mean PSNR value for green channel: {round(mean_psnr_g, 2)} dB") 
print(f"Mean PSNR value for red channel: {round(mean_psnr_r, 2)} dB") 