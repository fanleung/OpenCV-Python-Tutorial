import cv2
import numpy as np

img = cv2.imread('drawing.jpg')

# 1.按照指定的宽度、高度缩放图片
res = cv2.resize(img, (132, 150))
# 按照比例缩放，如x,y轴均放大一倍
res2 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

cv2.imshow('shrink', res), cv2.imshow('zoom', res2)
cv2.waitKey(0)


# 2.翻转图片

# 参数2=0：垂直翻转(沿x轴)，
# 参数2>0: 水平翻转(沿y轴)
# 参数2<0: 水平垂直翻转
dst = cv2.flip(img, -1)
# np.hstack: 横向并排，对比显示
cv2.imshow('flip', np.hstack((img, dst)))  # np.hstack: 横向并排，对比显示
cv2.waitKey(0)


# 3.平移图片
rows, cols = img.shape[:2]
# 定义平移矩阵，需要是 numpy 的 float32 类型
# x轴平移100，y轴平移50
# 仿射变换函数 cv2.warpAffine
M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('shift', dst)
cv2.waitKey(0)


# 4.45°顺时针旋转图片并缩小一半
# 参数1：图片的旋转中心
# 参数2：旋转角度(正：逆时针，负：顺时针)
# 参数3：缩放比例，0.5表示缩小一半
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), -45, 0.5)
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('rotation', dst)
cv2.waitKey(0)
