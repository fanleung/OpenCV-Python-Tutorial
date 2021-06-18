import cv2

img = cv2.imread('lena.jpg')

# 1.获取像素的值 y = 100, x = 90
px = img[100, 90]
print(px)  # [105 98 197] [B G R]

# 只获取蓝色 blue通道的值 img[100, 90, 0]
# 只获取蓝色 green 通道的值 img[100, 90, 1]
# 只获取蓝色 red 通道的值 img[100, 90, 2]
px_blue = img[100, 90, 0]
print(px_blue)  # 105


# 2.修改像素的值
# 只操作了内存的像素点，原图没有保存没有修改
img[100, 90] = [255, 255, 255]
print(img[100, 90])  # [255 255 255]


# 3.图片形状
print(img.shape)  # (263, 247, 3)
# 形状中包括行数、列数和通道数
height, width, channels = img.shape
# img是灰度图的话：height, width = img.shape

# 总像素数
print(img.size)  # 263*247*3=194883
# 数据类型
print(img.dtype)  # uint8


# 4.ROI截取
face = img[100:200, 115:188]
cv2.imshow('face', face)
cv2.waitKey(0)


# 5.通道分割与合并
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))
# split 比较耗时， 更推荐的获取某一通道方式
b = img[:, :, 0]
g = img[:, :, 1]
r = img[:, :, 2]
cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)
cv2.waitKey(0)
