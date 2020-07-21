import cv2

cap = cv2.VideoCapture('vtest.avi')
knn_sub = cv2.createBackgroundSubtractorKNN()
mog2_sub = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    mog_sub_mask = mog2_sub.apply(frame)
    knn_sub_mask = knn_sub.apply(frame)

    cv2.imshow('original', frame)
    cv2.imshow('MOG2', mog_sub_mask)
    cv2.imshow('KNN', knn_sub_mask)

    key = cv2.waitKey(30) & 0xff
    if key == 27 or key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()