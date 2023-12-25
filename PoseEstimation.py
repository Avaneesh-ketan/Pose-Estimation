import cv2 as cv
import mediapipe as mp
import time 

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils
#read video from camera
cap = cv.VideoCapture(0)
cTime =0
pTime = 0
while True:
    suc, img = cap.read()
    imgRBG = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = pose.process(imgRBG)
    cv.waitKey(1)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h,w,c = img.shape
            print(id, lm)
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv.putText(img, str(int(fps)), (10,70), cv.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3) #1) img, 2)displayable text 3) position 4) Font 5)Scale 6) Color 7)thickness
    cv.imshow("Image", img)