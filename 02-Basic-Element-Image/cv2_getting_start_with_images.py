import cv2

# 1.灰度图加载一张彩色图
# cv2.IMREAD_COLOR：彩色图，默认值(1)
# cv2.IMREAD_GRAYSCALE：灰度图(0)
# cv2.IMREAD_UNCHANGED：包含透明通道的彩色图(-1)
img = cv2.imread('lena.jpg', 0)


# 2.显示图片
cv2.imshow('lena', img)
cv2.waitKey(0)

# 先定义窗口，后显示图片
cv2.namedWindow('lena2', cv2.WINDOW_NORMAL)
cv2.imshow('lena2', img)
cv2.waitKey(0)


# 3.保存图片
cv2.imwrite('lena_gray.jpg', img)
