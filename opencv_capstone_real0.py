#캡스톤 1 , 움직이는 사물 인지 + 시리얼 통신 + 좌표값 생성 및 통신 가능 사용 
# 라이다센서를 이용 할 시 이 파일을 이용할 예정
# 라이다센서와 라이다센서의 slam지도 등 필요
import cv2
import numpy as np
#import serial

# 아두이노와 시리얼 통신을 위한 객체 생성
#ser = serial.Serial('/dev/ttyACM0', 9600)

# 좌표계 생성을 위한 초기 프레임 로드
cap = cv2.VideoCapture(0) # 추후 캠 연결 예정 
_, frame = cap.read()

# 좌표계 생성에 필요한 변수 초기화
prev_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
prev_pts = cv2.goodFeaturesToTrack(prev_gray, maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7) # 물체에 대한 정보 , 코너 , 각 , 블럭 사이즈
mask = np.zeros_like(frame)

while True:
    # 현재 프레임 로드
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 이전 좌표값으로 optical flow 계산
    next_pts, status, error = cv2.calcOpticalFlowPyrLK(prev_gray, gray, prev_pts, None, winSize=(15,15), maxLevel=2)
    
    # 이동된 좌표계 계산
    good_new = next_pts[status==1]
    good_old = prev_pts[status==1]
    
    # 이동된 좌표계 시각화
    for i, (new, old) in enumerate(zip(good_new, good_old)):
        a, b = new.ravel()
        c, d = old.ravel()
        mask = cv2.line(mask, (int(a), int(b)), (int(c), int(d)), (0, 255, 0), 2) # 위에서 계산한 좌표를 정수형으로 받아옴.
        frame = cv2.circle(frame, (int(a), int(b)), 5, (0, 0, 255), -1) 
        
    # 좌표계 시각화된 프레임 출력
    img = cv2.add(frame, mask)
    cv2.imshow("frame", img)
    
    # 좌표계 계산을 위한 현재 좌표값 저장
    prev_gray = gray.copy()
    prev_pts = good_new.reshape(-1, 1, 2)
    
    # 이동할 좌표를 계산하여 아두이노에게 전송
    if cv2.waitKey(1) & 0xFF == ord('c'):
        coords = np.mean(good_new, axis=0).astype(int)
        x, y = coords[0], coords[1]
        print(f"Moving to coordinates: ({x}, {y})")
        # 아두이노로 이동할 좌표값 전송
        #ser.write(f"{x},{y}\n".encode())
        
    # 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
#ser.close()