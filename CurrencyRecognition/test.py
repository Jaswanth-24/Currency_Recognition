
import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

for i in range(1,7):
    img_rgb = cv2.imread('testImages/'+str(i)+'.jpg')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    maxValue = 0
    flag = 0
    temps = None
    for root, dirs, directory in os.walk('Dataset'):
        for j in range(len(directory)):
            name = os.path.basename(root)
            if 'Thumbs.db' not in directory[j]:
                template = cv2.imread(root+"/"+directory[j],0)
                w, h = template.shape[::-1]
                img_gray = cv2.resize(img_gray,(w,h))
                img_rgb = cv2.resize(img_rgb,(w,h))
                res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
                threshold = 0.4
                loc = np.where( res >= threshold)