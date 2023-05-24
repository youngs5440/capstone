import cv2 

img = cv2.imread('xyzmap.jpg') #이미지는 python 폴더 안에 있는 xyzmap.jpg 이다 . 

x_pos,y_pos,width,height = cv2.selectROI("location", img, False) 
print("x_position , y_position : " , x_pos , y_pos)#왼쪽 상단의 좌표를 0,0 으로 잡고 x좌표가 오른쪽으로 가면 + , y좌표는 아래로 갈 수록 + 이다 
print("width, height : ", width, height) #사각형을 생성시 가로를 width , 세로를 height 값으로 가져온다 

cv2.destroyAllWindows()