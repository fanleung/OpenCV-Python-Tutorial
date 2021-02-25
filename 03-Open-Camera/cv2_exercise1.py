import cv2


def track_back(x):
    '''
    ### 回调函数，x表示滑块的位置
    '''
    # 更改视频的帧位置
    capture.set(cv2.CAP_PROP_POS_FRAMES, x)


cv2.namedWindow('window')

capture = cv2.VideoCapture('demo_video.mp4')
# 获取视频总共多少帧
frames = capture.get(cv2.CAP_PROP_FRAME_COUNT)
# 创建滑动条 5个参数
# 参数1：滑动条的名称
# 参数2：所在窗口的名称， 所以要先创建窗口
# 参数3：当前的值
# 参数4：最大值
# 参数5：回调函数名称，回调函数默认有一个表示当前值的参数
cv2.createTrackbar('process', 'window', 1, int(frames), track_back)

while(capture.isOpened()):
    ret, frame = capture.read()

    cv2.imshow('window', frame)
    if cv2.waitKey(30) == ord('q'):
        break
