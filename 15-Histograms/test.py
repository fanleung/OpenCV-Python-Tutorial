import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('hist.jpg', 0)

img_roi = img[:200, :200]

hist = cv2.calcHist([img_roi], [0], None, [256], [0, 256])

# plt.hist(img_roi.ravel(), 256, [0, 256])
# plt.show()

plt.plot(hist)
plt.show()