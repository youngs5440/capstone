import sys 
import numpy as np
import cv2

#영상의 이동 변환과 전단 변환 영상 가로 세로를 일정 크기만큼 이동 , (시프트연산)
src = cv2.imread('test1.jpg')

if src is None:
    print('Image load failed!')
    sys.exit()

w, h = 720, 400
srcQuad = np.array([[325, 307], [760, 369], [718, 611], [231, 515]], np.float32)
dstQuad = np.array([[0, 0], [w-1, 0], [w-1, h-1], [0, h-1]], np.float32)

pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
dst = cv2.warpPerspective(src, pers, (w, h)) #src은 이미지 의미 , M은 변환행렬 즉 pers , dsize는 w h 값을 현재 받고 있다  . 


cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()