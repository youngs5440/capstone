import cv2

# SLAM 지도 이미지 로드
slam_map = cv2.imread("slam_map.jpg")

# 클릭 이벤트 처리 함수
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # 클릭한 위치로 RC 카 이동
        move_rc_car(x, y)

# RC 카 이동 함수 (예시)
def move_rc_car(x, y):
    # RC 카 이동 코드 작성
    # 해당 위치로 RC 카를 이동시키는 로직을 구현합니다.
    # 이동된 RC 카의 위치를 업데이트하고 지도에 표시합니다.

# OpenCV 창 생성 및 마우스 콜백 등록
    cv2.namedWindow("SLAM Map")
    cv2.setMouseCallback("SLAM Map", mouse_callback)

while True:
    # 지도에 표시된 RC 카 위치를 출력
    cv2.imshow("SLAM Map", slam_map)
    
    # 'q' 키를 누르면 반복문 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()