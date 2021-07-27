#!/usr/bin/env python
from glob import glob
import cv2
pngs = glob('/Users/tallulahthompson/Downloads/Emotion-detection-master/src/data3/images/*.png')
singlepng = []
all = glob('/Users/tallulahthompson/Downloads/Emotion-detection-master/src/data3/images/**')

length = len(all)
count = 0
for i in range(0,length):
    all[i] = all[i].lstrip('/Users/tallulahthompson/Downloads/Emotion-detection-master/src/data3/images/')
    if all[i][-3:] == "png":
        count += 1
        singlepng.append(all[i])

for k in range(0,len(pngs)):
    first = pngs[k]
    img = cv2.imread(first)
    img = cv2.imwrite("data3/images2/" +singlepng[k] , img)


