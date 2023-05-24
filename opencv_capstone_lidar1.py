import cv2
import numpy as np

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
        # RC car moving code here

        # Reset click_x and click_y
        click_x = None
        click_y = None

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
