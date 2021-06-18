import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取灰度图
img = cv2.imread('hist.jpg', 0)


# 1.直方图计算
# 使用OpenCV函数计算
# 参数1：要计算的原图，以方括号的传入，如：[img]
# 参数2：类似前面提到的dims，灰度图写[0]就行，彩色图B/G/R分别传入[0]/[1]/[2]
# 参数3：要计算的区域，计算整幅图的话，写None
# 参数4：前面提到的bins
# 参数5：前面提到的range
hist = cv2.calcHist([img], [0], None, [256], [0, 256])  # 性能：0.022158 s

# 使用numpy函数计算
hist, bins = np.histogram(img.ravel(), 256, [0, 256])  # 性能：0.020628 s

# 使用numpy函数计算
hist = np.bincount(img.ravel(), minlength=256)  # 性能：0.003163 s


# 2.绘制直方图
plt.hist(img.ravel(), 256, [0, 256])
plt.show()

# 或使用前面计算的直方图结果
# plt.plot(hist)
# plt.show()


# 3.直方图均衡化
equ = cv2.equalizeHist(img)
cv2.imshow('equalization', np.hstack((img, equ)))  # 并排显示
cv2.waitKey(0)

# 绘制出均衡化后的直方图
plt.hist(equ.ravel(), 256, [0, 256])
plt.show()


# 4.自适应直方图均衡化
img = cv2.imread('tsukuba.jpg', 0)
equ = cv2.equalizeHist(img)  # 应用全局直方图均衡化

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))  # 自适应均衡化，参数可选
cl1 = clahe.apply(img)

cv2.imshow('equalization', np.hstack((equ, equ, cl1)))  # 并排显示
cv2.waitKey(0)
