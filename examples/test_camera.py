import cv2
import time

time.sleep(2)
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('original', frame)

    key = cv2.waitKey(1) & 0xff
    if key == 27 or key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()