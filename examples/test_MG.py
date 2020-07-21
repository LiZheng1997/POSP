import cv2

capture = cv2.VideoCapture(r"vtest.avi")
mog = cv2.createBackgroundSubtractorMOG2()
se = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

while True:
    ret, image = capture.read()
    if ret is True:
        fgmask = mog.apply(image)
        ret, binary = cv2.threshold(fgmask, 220, 255, cv2.THRESH_BINARY)
        binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, se)
        backgimage = mog.getBackgroundImage()
        cv2.imshow("backgimage", backgimage)
        cv2.imshow("frame", image)
        cv2.imshow("binary", binary)
        c = cv2.waitKey(50)
        if c == 27:
            break
    else:
        break