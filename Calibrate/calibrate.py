import cv2
import os
import numpy as np
from PIL import Image
from array import *

path = "C:\dev\hth\\test\\"
cap = cv2.VideoCapture(0)

paintWindow = np.zeros((471,636,3)) + 255
paintWindow = cv2.rectangle(paintWindow, (40,1), (140,65), (0,0,0), 2)


while(True):

    #rect not coming on
    (grabbed, frame) = cap.read()
    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Add the coloring options to the frame
    frame = cv2.rectangle(frame, (270,190), (370,290), (255,0,0), 2)
    cv2.imshow("Tracking", frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        out = cv2.imwrite(os.path.join(path , 'sensor.jpg'), frame)
        break

cap.release()
cv2.destroyAllWindows()

path+="sensor.jpg"

im = Image.open(path)

# Change these values to fit the size of your region of interest
width, height = im.size #get image size


# since you do not specify the size of the center area in the question, just replace the below variables with what you want
left = int((width/2)-50)
top = int((height/2)-50)
right = int((width/2)+50)
bottom = int((height/2)+50)
cv2.rectangle(im, (left,top), (right,bottom), (255,0,0))

cropped = im.crop((left, top, right, bottom)) #crop the center of the image
rgb = cropped.convert('RGB')  # get three R G B values
print(rgb)



value=[[]]
for x in range(0, 99):
    for y in range(0, 99):
        r, g, b = rgb.getpixel((x, y))
        value.append([[r,g,b]])

value.sort()

print(value[1])
print(value[9801])



