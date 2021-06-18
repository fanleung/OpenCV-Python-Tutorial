import cv2
import numpy as np

# 创建一副黑色的图片
# 大小是 512x512
img = np.zeros((512, 512, 3), np.uint8)

# 1.画一条线宽为5的蓝色直线，参数2：起点，参数3：终点
# img, 起点， 终点， 颜色， 宽度
cv2.line(img, (0, 0), (512, 512), (255, 0, 0), 5)


# 2.画一个绿色边框的矩形，参数2：左上角坐标，参数3：右下角坐标
# img, 左上角坐标， 右下角坐标， 颜色， 宽度
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)


# 3.画一个填充红色的圆，参数2：圆心坐标，参数3：半径
# img, 圆心坐标， 半径， 颜色， 宽度（-1是填充）
cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)


# 4.在图中心画一个填充的半圆
# 画椭圆
# img, 圆心坐标, x/y长度， 旋转角度， 起始角度，结束角度，颜色，宽度
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, (255, 0, 0), -1)


# 5.画一个闭合的四边形
# 定义四个顶点坐标
pts = np.array([[10, 5],  [50, 10], [70, 20], [20, 30]], np.int32)
print(pts.shape)
print(pts)
# 顶点个数：4，矩阵变成 4*1*2 维（注意 numpy 中 -1 的用法）
# 1. numpy中 -1 是让数组横向平铺
# 2. OpenCV中需要先将多边形的顶点坐标需要变成顶点数×1×2维的矩阵，再来绘制
pts = pts.reshape((-1, 1, 2))
print(pts.shape)
print(pts)

# 如果第三个参数是 False，多边形就不闭合
cv2.polylines(img, [pts], True, (0, 255, 255))


# 使用cv2.polylines()画多条直线
line1 = np.array([[100, 20],  [300, 20]], np.int32).reshape((-1, 1, 2))
line2 = np.array([[100, 60],  [300, 60]], np.int32).reshape((-1, 1, 2))
line3 = np.array([[100, 100],  [300, 100]], np.int32).reshape((-1, 1, 2))
cv2.polylines(img, [line1, line2, line3], True, (0, 255, 255))


# 6.添加文字
# img, 文本， 起始坐标， 字体， 大小，颜色, 粗细， LINE_AA 抗锯齿
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'ex2tron', (10, 500), font,
            4, (255, 255, 255), 5, lineType=cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey(0)
