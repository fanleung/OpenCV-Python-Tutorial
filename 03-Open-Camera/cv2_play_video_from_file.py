import cv2

# 播放本地视频
capture = cv2.VideoCapture('demo_video.mp4')

while(capture.isOpened()):
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    # cv2.waitKey(), 它的参数表示暂停时间，值越大，播放速度越慢。反之值越小，播放速度越快，一般定为 30
    if cv2.waitKey(30) == ord('q'):
        break
