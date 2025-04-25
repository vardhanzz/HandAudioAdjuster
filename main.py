import cv2 as cv
import time
import numpy as np
import HandTrackingModule as htm
import math
import subprocess


wCam, hCam = 640, 480  

cap = cv.VideoCapture(0) 
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.7)

vol = 0
volBar = 400
volPer = 0

def set_volume(volume):

    script = f"set volume output volume {volume} --100 to 100"
    subprocess.run(["osascript", "-e", script])

while True:
    success, img = cap.read()
    
    if not success:
        print("Failed to grab frame.")
        break

    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        
            x1, y1 = lmList[4][1], lmList[4][2]  
            x2, y2 = lmList[8][1], lmList[8][2]  
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

            cv.circle(img, (x1, y1), 15, (0, 0, 255), cv.FILLED)
            cv.circle(img, (x2, y2), 15, (0, 0, 255), cv.FILLED)
            cv.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
            cv.circle(img, (cx, cy), 15, (255, 0, 255), cv.FILLED)

            length = math.hypot(x2 - x1, y2 - y1)

            vol = np.interp(length, [50, 270], [0, 100])
            volBar = np.interp(length, [50, 270], [400, 150])
            volPer = np.interp(length, [50, 270], [0, 100])

            
            set_volume(int(vol))

            if length < 50:
                cv.circle(img, (cx, cy), 15, (0, 255, 0), cv.FILLED)


    cv.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
    cv.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv.FILLED)
    cv.putText(img, f'{int(volPer)} %', (40, 450),
                cv.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

  
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv.putText(img, f'FPS: {int(fps)}', (40, 50),
                cv.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

 
    cv.imshow("Img", img)

    if cv.waitKey(20) & 0xFF == ord('d'):  
        break


cap.release()
cv.destroyAllWindows()
