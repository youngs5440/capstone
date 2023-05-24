import cv2
import numpy as np
import math
#import serial
import time

# 시리얼 통신을 위한 객체 생성
#ser = serial.Serial('COM3', 9600)

# 마우스 클릭 이벤트 핸들러 함수
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # 클릭한 좌표 출력
        print("Clicked at x={}, y={}".format(x, y))

        # rc카로 보낼 좌표값 계산
        x_coord = x
        y_coord = y

        # rc카로 보낼 좌표값 출력
        print("Move to x={}, y={}".format(x_coord, y_coord))

        # rc카로 좌표값 전송
        #ser.write("{} {}$".format(x_coord, y_coord).encode())

# 웹캠에서 영상을 가져오기 위한 객체 생성
cap = cv2.VideoCapture(0)

# 마우스 클릭 이벤트 콜백 함수 등록
cv2.namedWindow("WebCam")
cv2.setMouseCallback("WebCam", mouse_callback)

while True:
    # 웹캠으로부터 영상 프레임을 가져옴
    ret, frame = cap.read()

    # 노이즈 줄이는 함수 +  엣지 검출
    blur = cv2.GaussianBlur(frame, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150, apertureSize=3)

    # 검출된 선 그리기
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=50)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # 영상처리 화면 띄우기
    cv2.imshow("WebCam", frame)

    # q 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 객체 해제
cap.release()
cv2.destroyAllWindows()