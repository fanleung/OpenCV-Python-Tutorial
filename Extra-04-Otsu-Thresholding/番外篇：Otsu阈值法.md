可以看到，Otsu阈值明显优于固定阈值，省去了不断尝试阈值判断效果好坏的过程。

其中，绘制直方图时，使用了numpy中的ravel()函数，它会将原矩阵压缩成一维数组，便于画直方图。


g就是前景与背景两类之间的方差，这个值越大，说明前景和背景的差别也就越大，效果越好。Otsu算法便是遍历阈值T，使得gg最大，所以又称为最大类间方差法。基本上双峰图片的阈值T在两峰之间的谷底。