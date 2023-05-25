import cv2

# SLAM 지도 이미지 로드
slam_map = cv2.imread("slam_map.jpg")

while True:
    # RC 카 위치 좌표 업데이트 (예시)
    rc_car_position = (100, 200)

    # RC 카 위치를 지도 이미지에 표시
    cv2.circle(slam_map, rc_car_position, 5, (0, 255, 0), -1)

    # 지도에 표시된 RC 카 위치를 출력
    cv2.imshow("SLAM Map", slam_map)
    
    # 'q' 키를 누르면 반복문 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()