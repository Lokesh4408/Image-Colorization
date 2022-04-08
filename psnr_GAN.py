import cv2
import os
from math import log10, sqrt 
import numpy as np 

# Define original and colorized paths:
path_original = '/home/lokesh/Desktop/mediaSubjects/IVP/avt_image_db/'
path_colorized = '/home/lokesh/Desktop/mediaSubjects/IVP/objectiveMetrics/avt_image_db_chromagan/'

psnr_sum = 0
counter = 0
for filename in os.listdir(path_original):
    if filename.endswith('.png') or filename.endswith('.jpg'):
        original = cv2.imread(f'{path_original}/{filename}')

        original_name = os.path.basename(filename)
        original_name = original_name.split('.')[0]+"psnr" #instead of removing psnr from the result images, we have added 'psnr' under the original name 

        # Search for the image in the colorized folder:
        for filename_colorized in os.listdir(path_colorized):
            if filename_colorized.endswith('.png') or filename_colorized.endswith('.jpg'):

                colorized_name = os.path.basename(filename_colorized)
                if "_" in colorized_name:
                    colorized_name = colorized_name.split('_')[2]
                colorized_name = colorized_name.split('.')[0]

                if colorized_name == original_name:
                    print("match")
                    colorized = cv2.imread(f'{path_colorized}/{filename_colorized}')
                    # with break it stops searching for the right picture
                    # --> breaks current for loop
                    break
        mse = np.mean((original - colorized) ** 2) 
        if(mse == 0):  # MSE is zero means no noise is present in the signal . 
                       # Therefore PSNR have no importance. 
            pnsr_sum = 100
        max_pixel = 255.0
        psnr_sum += 20 * log10(max_pixel / sqrt(mse))
        print(psnr_sum)
        counter += 1

mean_psnr = psnr_sum / counter 
print(f"Mean PSNR value is {mean_psnr} dB") 