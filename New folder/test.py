import cv2
import time
import keyboard
import vlc
import random
#This part for taking a picture from webcam or camera
cam = cv2.VideoCapture(0)
res,frame = cam.read()
img_name = "screenshot.png"
cv2.imwrite(img_name,frame)
cam.release()

#Fuction to play a video
def playVideo(d):
    media_player = vlc.MediaPlayer()
    media = vlc.Media(d)
    media_player.set_media(media)
    media_player.play()
    time.sleep(1)
    while media_player.is_playing():    
        if keyboard.is_pressed(" "):
            break
        else:
            time.sleep(0.01)

#here we detect objects using coco.names
img = cv2.imread('screenshot.png')
classNames = []
classFile = 'coco.names'
with open(classFile,'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')
configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'
net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5,127.5,127.5))
net.setInputSwapRB(True)   
classIds, confs, bbox = net.detect(img,confThreshold=0.5)
print(classIds)
L = list(classIds)
ci =[]
cs =[]
for i in L:
    if i not in ci:
        ci.append(i)
        cs.append(L.count(i))
print(ci,cs)
obj = ci[cs.index(max(cs))]
print(obj)
if len(classIds != 0):
    for classIds, confidence, box in zip(classIds.flatten(),confs.flatten(),bbox):
            cv2.rectangle(img, box, color = (0,255,0),thickness = 2)
            cv2.putText(img,classNames[classIds -1],(box[0]+10,box[1]+30),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),2)

persons = ["person1.mp4","person2.mp4"]
cars = ["car1.mp4","car2.mp4","car3.mp4"]
bird = ["bird1.mp4","bird2.mp4","bird3.mp4"]
train = ["train1.mp4","train2.mp4"]

if obj == 1:
    playVideo(random.choice(persons))
elif obj == 3:
    playVideo(random.choice(cars))
elif obj == 16:
    playVideo(random.choice(bird))
elif obj == 7:
    playVideo(random.choice(train))
cv2.waitKey(0)