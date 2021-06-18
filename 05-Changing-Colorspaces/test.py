import cv2
# cap = cv2.VideoCapture("rtsp://admin:admin@192.168.1.102:554//Streaming/Channels/1")
# cap = cv2.VideoCapture("http://admin:admin@192.168.1.102:8554")
cap = cv2.VideoCapture("http://admin:admin@192.168.42.129:8081")
# cap = cv2.VideoCapture("rtsp://admin:admin@192.168.1.102:8554/live")
ret,frame = cap.read()
print(ret)
while ret:
    ret,frame = cap.read()
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
