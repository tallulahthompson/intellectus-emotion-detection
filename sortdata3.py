import cv2
import glob
import pandas as pd
data = pd.read_csv("legend.csv")
##print(data)
pngs = glob.glob('/Users/tallulahthompson/Downloads/Emotion-detection-master/src/data3/images2/*.png')
##print(pngs)
singlepng = []
for i in range(0,len(pngs)):
    singlepng.append(pngs[i].strip("/Users/tallulahthompson/Downloads/Emotion-detection-master/src/data3/images2/"))
    singlepng[i]+="png"

angry = 4002
sad = 4840
happy = 7222
neutral = 4698
surprised = 3176
fearful = 4109
disgust = 445

for i in range(0,len(singlepng)):
    first_emotion = data.loc[:,"emotion"][i]
    first_image = data.loc[:,"image"][i]
    first_image = first_image.strip("jpg")
    first_image += "png"
    first_emotion = first_emotion.upper()
    if first_emotion == "ANGER":
        for j in range(0,len(singlepng)):
            if first_image == singlepng[j]:
                image = pngs[j]
                img = cv2.imread(image)
                img = cv2.resize(img, (48, 48))
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                img = cv2.imwrite("data/train/angry/im" +str(angry)+".png", img)
                angry += 1
    elif first_emotion == "DISGUST":
        for j in range(0,len(singlepng)):
            if first_image == singlepng[j]:
                image = pngs[j]
                img = cv2.imread(image)
                img = cv2.resize(img, (48, 48))
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                img = cv2.imwrite("data/train/disgusted/im" + str(disgust) + ".png", img)
                disgust += 1
    elif first_emotion == "HAPPINESS":
        for j in range(0,len(singlepng)):
            if first_image == singlepng[j]:
                image = pngs[j]
                img = cv2.imread(image)
                img = cv2.resize(img, (48, 48))
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                img = cv2.imwrite("data/train/happy/im" + str(happy) + ".png", img)
                happy += 1
    elif first_emotion == "NEUTRAL":
        for j in range(0,len(singlepng)):
            if first_image == singlepng[j]:
                image = pngs[j]
                img = cv2.imread(image)
                img = cv2.resize(img, (48, 48))
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                img = cv2.imwrite("data/train/neutral/im" + str(neutral) + ".png", img)
                neutral += 1
    elif first_emotion == "SADNESS":
        for j in range(0,len(singlepng)):
            if first_image == singlepng[j]:
                image = pngs[j]
                img = cv2.imread(image)
                img = cv2.resize(img, (48, 48))
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                img = cv2.imwrite("data/train/sad/im" + str(sad) + ".png", img)
                sad += 1
    elif first_emotion == "FEAR":
        for j in range(0,len(singlepng)):
            if first_image == singlepng[j]:
                image = pngs[j]
                img = cv2.imread(image)
                img = cv2.resize(img, (48, 48))
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                img = cv2.imwrite("data/train/fearful/im" + str(fearful) + ".png", img)
                fearful += 1
    elif first_emotion == "SURPRISE":
        for j in range(0,len(singlepng)):
            if first_image == singlepng[j]:
                image = pngs[j]
                img = cv2.imread(image)
                img = cv2.resize(img, (48, 48))
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                img = cv2.imwrite("data/train/surprised/im" + str(surprised) + ".png", img)
                surprised += 1