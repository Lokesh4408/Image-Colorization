import cv2

originalImage = cv2.imread('/home/lokesh/Desktop/mediaSubjects/IVP/train/a1Zj8R9J.png')
print('Original dimensions:', originalImage.shape)

scale_percent = 10
width = int(originalImage.shape[1] * scale_percent / 100)
height = int(originalImage.shape[0] * scale_percent / 100)
dim = (width, height)

resized = cv2.resize(originalImage, dim, interpolation = cv2.INTER_AREA)
print('Resized dimensions:', resized.shape)

grayImage = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('Black white image', blackAndWhiteImage)
#cv2.imshow('Original image',originalImage)
cv2.imshow('Gray image', grayImage)
cv2.imwrite("gray_a1Zj8R9J.png", grayImage)
cv2.waitKey(50000) #desired waiting time
cv2.destroyAllWindows()