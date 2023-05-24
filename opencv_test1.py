import cv2

image = cv2.imread("test1.jpg",cv2.IMREAD_COLOR)
cv2.imshow("TEST",image) #이미지 처리 창 이름을 test 로 정할것
cv2.waitKey(0)
cv2.destroyAllWindows()