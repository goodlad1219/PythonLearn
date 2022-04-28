import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0) #create video capture update
cap.set(3, 1280) #set(propid, value), prop id for width is 3.
cap.set(4, 720) #set(propid, value), prop id for height is 4.

detector = HandDetector(detectionCon=0.8, maxHands=1) #detection confidence is bydefault 0.5

keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]]

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
    hands, img = detector.findHands(img) # find hands
    # bboxInfo = detector.findPositions(img) #landmark points

    # Draws the buttons
    img = drawALL(img,buttonList)

     



    cv2.imshow("Image", img)
    # closes the window if we pres  q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

 