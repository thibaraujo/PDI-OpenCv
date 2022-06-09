import cv2
import numpy as np

# GLOBALS
directory = './tomato.jpg'   
image = cv2.imread(directory, 1)  
aux_img = cv2.imread(directory, 1)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) 
kernel1 = np.ones((3, 3), np.uint8)
kernel2 = np.ones((10, 10), np.uint8)

# FILTERS
blur = cv2.blur(image, (2, 2)) #not used in this case
median = cv2.medianBlur(image, 11) # not used in this case
gaussian = cv2.GaussianBlur(image, (21, 21), 1)

# RED'S MASK
red1 = cv2.inRange(hsv, (0, 50, 200), (10, 255, 255))
red2 = cv2.inRange(hsv, (160, 50, 200), (179, 255, 255))
selection = cv2.add(red1, red2)

# TREATMENT
opening = cv2.morphologyEx(selection, cv2.MORPH_OPEN,kernel1)
dilation = cv2.dilate(opening, kernel2, iterations=1)
result = cv2.bitwise_and(gaussian, gaussian, mask=dilation)

# CONTORN
gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
contorn, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
output = cv2.drawContours(image, contorn, -1, (255, 0, 0), 3)
write = cv2.putText(output,"Tomato",(180,120),cv2.FONT_HERSHEY_TRIPLEX,1,255)

# PRINT STEPS
imgs = [cv2.imshow("INPUT", aux_img),cv2.imshow("Gaussian filter", gaussian), cv2.imshow("Red Mask", selection), cv2.imshow("Treatment", result), cv2.imshow("OUTPUT", write) ]
for i in imgs:
    i
    cv2.waitKey(0)
    
