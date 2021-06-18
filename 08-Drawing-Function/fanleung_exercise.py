import cv2
import numpy as np
# 创建一副黑色的图片
# 大小是 512x512
img = np.zeros((256, 256, 3), np.uint8)

# 画椭圆
# img, 圆心坐标, x/y长度， 旋转角度， 起始角度，结束角度，颜色，宽度
cv2.ellipse(img, (128, 50), (50, 50), 120, 0, 300, (0, 0, 255), -1,lineType=cv2.LINE_AA)
cv2.circle(img, (128, 50), 25, (0, 0, 0), -1,lineType=cv2.LINE_AA)

cv2.ellipse(img, (50, 206), (50, 50), 0, 0, 300, (0, 255, 0), -1,lineType=cv2.LINE_AA)
cv2.circle(img, (50, 206), 25, (0, 0, 0), -1,lineType=cv2.LINE_AA)

cv2.ellipse(img, (256-52, 206), (50, 50), 300, 0, 300, (255, 0, 0), -1,lineType=cv2.LINE_AA)
cv2.circle(img, (256-52, 206), 25, (0, 0, 0), -1,lineType=cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey(0)