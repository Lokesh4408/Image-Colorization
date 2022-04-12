import cv2
import os

input_directory = '/Users/Lokesh/Documents/IVP/colorization/uncropped'
output_directory = 'cropped'

for filename in os.listdir(input_directory):
    if filename.endswith('.png') or filename.endswith('.jpg'):
        img = cv2.imread(f'{input_directory}/{filename}')
        y = int(img.shape[0]/2)
        crop_img = img[0:y, :]
        if not cv2.imwrite(f'{output_directory}/cropped_{filename}', crop_img):
             raise Exception("Could not write image")

