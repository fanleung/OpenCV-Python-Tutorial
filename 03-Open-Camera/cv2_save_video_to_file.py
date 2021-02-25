import cv2

capture = cv2.VideoCapture(0)

# 定义编码方式并创建 VideoWriter 对象
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
# fourcc = cv2.VideoWriter_fourcc('M','J','P','G')

# VideoWriter 四个参数
# 输出文件名，如 'output.avi'
# 编码方式 FourCC 码
# 帧率 FPS
# 要保存的分辨率大小
outfile = cv2.VideoWriter('output.avi', fourcc, 25., (640, 480))

while(capture.isOpened()):
    ret, frame = capture.read()

    if ret:
        # 写入文件
        outfile.write(frame)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break
