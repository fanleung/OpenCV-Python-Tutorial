import cv2
import numpy as np

# blue HSV
blue = np.uint8([[[255, 0, 0]]])
hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
print(hsv_blue)

# green HSV
green = np.uint8([[[0, 255, 0]]])
hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
print(hsv_green)

# red HSV
red = np.uint8([[[0, 0, 255]]])
hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
print(hsv_red)

# blue  [[[120 255 255]]]
# green [[[ 60 255 255]]]
# red   [[[  0 255 255]]]

# 蓝色的范围
lower_blue = np.array([100, 110, 110])
upper_blue = np.array([130, 255, 255])

# 绿色的范围
lower_green = np.array([40, 90, 90])
upper_green = np.array([70, 255, 255])

# 红色的范围
lower_red = np.array([160, 120, 120])
upper_red = np.array([179, 255, 255])

