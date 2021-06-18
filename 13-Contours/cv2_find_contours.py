import cv2

img = cv2.imread('handwriting.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 使用Otsu自动阈值，注意用的是cv2.THRESH_BINARY_INV
ret, thresh = cv2.threshold(
    img_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)


# 寻找轮廓
# 输入： img， 轮廓的查找方式，轮廓的近似方式
# 返回：找到的轮廓， 轮廓层级关系
contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print(contours)

cnt = contours[1]

# 绘制轮廓
# 参数1： img
# 参数2：得到的轮廓
# 参数3： -1 表示绘制所有轮廓，否则绘制第几条，从0开始
# 参数4： 颜色
# 参数5：粗细
# cv2.drawContours(img, [cnt], 0, (0, 0, 255), 2)
cv2.drawContours(img, contours, -1, (0, 0, 255), 2)

cv2.imshow('contours', img)
cv2.waitKey(0)
