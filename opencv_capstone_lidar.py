import cv2
import numpy as np
import time
#import serial
#rospy 추가예정

# RC카 인식
def detect_car(frame):
    # BGR to HSV (HSV 컬러 스페이스를 이용해서 빨간색 자동차 인식 )
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 설정 범위  (빨간색 차량 인식 , apply mask)
    mask = cv2.inRange(hsv, (0, 70, 50), (10, 255, 255))

    # 설정 범위 ( 빨간색 차량 ,apply mask)
    mask2 = cv2.inRange(hsv, (170, 70, 50), (180, 255, 255))

    #  <mask 합치기 물체인식>
    mask = cv2.addWeighted(mask, 1.0, mask2, 1.0, 0.0)

    # Apply blur and find contours <등고선 찾기>
    mask = cv2.medianBlur(mask, 7)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 인식 범위
    max_area = 0
    max_contour = None
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > max_area:
            max_area = area
            max_contour = contour

    # Find center of contour
    if max_contour is not None:
        moment = cv2.moments(max_contour)
        cx = int(moment['m10'] / moment['m00'])
        cy = int(moment['m01'] / moment['m00'])
        return cx, cy

    return None, None
#xy 좌표를 받고 rc카가 이동 
def move_car(x, y, ser):
    # 속도 , 제어 
    speed = 100
    direction = 'stop'

    if x is not None and y is not None:
        # turn 값 계산
        turn = (x - 320) / 320.0

        # 왼쪽 오른쪽 커브 조건문
        if turn < -0.1:
            direction = 'left'
        elif turn > 0.1:
            direction = 'right'
        else:
            direction = 'forward'

        # rc car에 명령 전달 
        command = '{}:{}\n'.format(direction, speed)
        ser.write(command.encode())
        print('Sent command:', command)

 # 클릭한 위치의 xy 좌표가 등장 , 
click_x = None
click_y = None

def mouse_callback(event, x, y, flags, param):
    global click_x, click_y
    if event == cv2.EVENT_LBUTTONDOWN:
        click_x, click_y = x, y
        print("Clicked:", click_x, click_y)

cap = cv2.VideoCapture(0)

cv2.namedWindow("frame")
cv2.setMouseCallback("frame", mouse_callback)

while True:
    ret, frame = cap.read()
    cv2.imshow("frame", frame)

    if click_x is not None and click_y is not None:
        print("Moving to:", click_x, click_y)
        # RC car 이동 코드

        # 클릭 좌표 초기화 
        click_x = None
        click_y = None
 #Q를 꾹 누르면 영상처리 종료
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
