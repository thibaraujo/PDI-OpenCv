import cv2
import numpy as np

# GLOBALS
directory = './base.png' 
kernel = np.ones((1,1), np.uint8)
image = cv2.imread(directory, 1) #leitura da imagem, flag = 1: colorida
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# FILTERS
blur = cv2.blur(image, (2,2))

# RED MASK
red1 = cv2.inRange(hsv, (0, 150, 190), (8, 240, 210))
red2 = cv2.inRange(hsv, (175, 150, 190), (179, 240, 210))
selection = cv2.add(red1, red2)

# TREATMENT
dilation = cv2.dilate(selection, np.ones((3,3), np.uint8), iterations=1)
result = cv2.bitwise_and(blur, blur, mask = dilation)

# PRINTING STEPS
imgs = [cv2.imshow("Image Base", image),cv2.imshow("Blur Filter", blur), cv2.imshow("Red Mask", selection), cv2.imshow("Output", result)]
for i in imgs:
    i
    cv2.waitKey(0)
    

