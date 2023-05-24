import cv2
import numpy as np

img = cv2.imread('xyzmap.jpg')
res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

#OR

height, width = img.shape[:2]
res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC) # resize는 img , dsize , fx , fy , interpolation 즉 이미지 , manual size 가로 세로 , 가로 배수 , 세로 배수 , 보간법이다  