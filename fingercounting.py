import cv2
import os
import HandTrackingModule as htm

wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    fingers = []
    if len(lmList) != 0:

        if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)


        totalFingers = fingers.count(1)
        print(totalFingers)

        cv2.putText(img, str(int(totalFingers)), (70, 130),
                    cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 255), 5)

    cv2.imshow("image", img)
    cv2.waitKey(1)