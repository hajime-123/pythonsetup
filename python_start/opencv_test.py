# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 11:34:25 2021

@author: 18530
"""

import cv2

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while( cap.isOpened() ):

    ret, frame = cap.read()
    cv2.imshow('Capture',frame)
    key = cv2.waitKey(1)
    #print( '%08X' % (key&0xFFFFFFFF) )
    if key & 0x00FF  == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


