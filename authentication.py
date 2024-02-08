import cv2
import numpy as np
from pyzbar.pyzbar import decode

img  = cv2.imread('1.png')
cp = cv2.VideoCapture(0)
cp.set(3,640)
cp.set(4,480)

with open('mydata.text') as f:
    mydatalist = f.read().splitlines()

print(mydatalist)

while True:
    success, img = cp.read()
    for barcode in decode(img):
        print(barcode.data)
        mydata = barcode.data.decode('utf-8')
        print(mydata)

        if mydata in mydatalist:
            myoutput = 'Authorised'
            mycol = (0,255,0)
        else:
            myoutput = 'Un-Authorised'
            mycol = (0, 255, 255)
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,mycol,5)
        pts2 = barcode.rect
        cv2.putText(img,myoutput,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,mycol,2)

    cv2.imshow('Result',img)
    cv2.waitKey(1)

