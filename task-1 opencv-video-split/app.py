import cv2
import json
cap= cv2.VideoCapture(0)
with open('users.json','r') as f:
    data = json.load(f)

ret, image = cap.read()
x1=data['x1']
x1=int(x1)
x2=data['x2']
x2=int(x2)
y1=data['y1']
y1=int(y1)
y2=data['y2']
y2=int(y2)
x3=data['x3']
x3=int(x3)
y3=data['y3']
y3=int(y3)
x4=data['x4']
x4=int(x4)
y4=data['y4']
y4=int(y4)
x5=data['x5']
x5=int(x5)
x6=data['x6']
x6=int(x6)
y5=data['y5']
y5=int(y5)
y6=data['y6']
y6=int(y6)
x7=data['x7']
x7=int(x7)
x8=data['x8']
x8=int(x8)
y7=data['y7']
y7=int(y7)
y8=data['y8']
y8=int(y8)



while True :
    photo = cap.read()[1]           # Storing the frame in a variable photo
    photo = cv2.flip(photo,1)       # Fliping the photo for mirror view
    cropu1 = photo[x1:x2,y1:y2]      # Top left part of the photo
    cropu2 = photo[x3:x4,y3:y4]       # Top right part of the photo
    cropd1 = photo[x5:x6,y5:y6]      # Bottom left part of the photo
    cropd2 = photo[x7:x8,y7:y8]       # Bottom right part of the photo
    cv2.imshow("cropu1",cropu1)     # It will show cropu1 part in a window     
    cv2.imshow("cropu2",cropu2)     # It will show cropu2 part in a window
    cv2.imshow("cropd1",cropd1)     # It will show cropd1 part in a window
    cv2.imshow("cropd2",cropd2)     # It will show cropd2 part in a window
    cv2.imshow("Live",photo)        # It will show complete video in a window
    if cv2.waitKey(50) == 13 :      # Specifying (Enter) button to break the loop
        break
cv2.destroyAllWindows() 
cap.release()