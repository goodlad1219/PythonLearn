import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
import time

cap = cv2.VideoCapture(0) #create video capture update --- id number = 0 - its the web cam id
cap.set(3, 1280) #set(propid, value), prop id for width is 3.
cap.set(4, 720) #set(propid, value), prop id for height is 4.

pTime = 0

detector = HandDetector(detectionCon=0.8, maxHands=1) #detection confidence is bydefault 0.5

keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]]

finalText = ""

def drawALL(img,buttonList):
    for button in buttonList:
        x,y = button.pos
        w,h = button.size
        cv2.rectangle(img, button.pos, (x+w,y+h), (255,0,255), cv2.FILLED )
        cv2.putText(img, button.text, (x+20,y+65), cv2.FONT_HERSHEY_PLAIN,4,(255,255,255), 4)

    return img


# class  to create button
class Button():
    def __init__(self, pos, text, size=[85,85]):
        self.pos = pos
        self.size = size
        self.text = text
        

buttonList = []
for x in range(len(keys)):
        for i,key in enumerate(keys[x]):
            buttonList.append(Button([100*i+50,100*x], key ))


#boilerplate for running webcam
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1) #flip the read image
    hands, img = detector.findHands(img, flipType= False) # find hands
    # bboxInfo = detector.findPositions(img) #landmark points

    # To show the frame rate.
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS:{int(fps)}', (80,120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Draws the buttons
    img = drawALL(img,buttonList)

    if hands:

        hand1 = hands[0]
        lmlist1 = hand1["lmList"] # List of 21 landmark points
        # bbox = hand1["bbox"] # Bounding box info x, y, w, h

        
        for button in buttonList:
            x, y = button.pos
            w, h = button.size

            # value of x of fingertip = lmList[8<landing point number>][0<axis number>]

            if (x < lmlist1[8][0] < x+w) and (y < lmlist1[8][1] < y+h):
                cv2.rectangle(img, button.pos, (x+w,y+h), (175,0,175), cv2.FILLED )
                cv2.putText(img, button.text, (x+20,y+65), cv2.FONT_HERSHEY_PLAIN,4,(255,255,255), 4)
                length, info = detector.findDistance(lmlist1[8],lmlist1[12],img=None)
                print(length)
                
                # When Clicked
                if length < 30:
                    cv2.rectangle(img, button.pos, (x+w,y+h), (0,255,0), cv2.FILLED )
                    cv2.putText(img, button.text, (x+20,y+65), cv2.FONT_HERSHEY_PLAIN,4,(255,255,255), 4)

                    finalText += button.text
                    sleep(0.15)
                
    cv2.rectangle(img, (50,350), (700,450), (175,0, 175), cv2.FILLED )
    cv2.putText(img, finalText, (60,425), cv2.FONT_HERSHEY_PLAIN,5,(255,255,255), 5)           
        
    cv2.imshow("SDP", img)

    # closes the window if we pres  Escape key
    # Ascii key code for Escape is 27
    if cv2.waitKey(1) & 0xFF == 27:
        break

 