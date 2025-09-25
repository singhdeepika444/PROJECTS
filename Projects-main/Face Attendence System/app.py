import cv2
import face_recognition
import numpy as np
import os
from datetime import datetime
import pandas as pd

#first step import images and convert them into RGB
imagePath="E:/My Projects/Face Attendence System/TrainingImage" 
images=[] # store images
imageName=[] # take name from image name itself
dayName=['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY'] # for writing day in attendence sheet
myList=os.listdir(imagePath)
#print(myList)
for cl in myList:
    currentImage=cv2.imread(f'{imagePath}/{cl}') # openCV function to read images
    images.append(currentImage)
    imageName.append(os.path.splitext(cl)[0]) # [0]th element contain name that we require
#print(imageName)

# face_recognition is based on dlib
def findEncodings(images): # dlib encode faces on128 feature.
    # finds 128 unique point from face  
    encodeList=[] # store encodings of all images in trainingImage folder
    for img in images: 
        # image is read through cv2 and we get images in BGR format and so we need to convert in RGB
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) 
        encode=face_recognition.face_encodings(img)[0] # find encoding of each training image
        encodeList.append(encode) # store each encode in list
    return encodeList
        
def markAttendence(name):
    with open('attend.csv','r+') as f:
        attendesData=f.readlines()
        #print(attendesData)
        nameList=[]
        for line in attendesData:
            entry=line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now=datetime.now()
            date=now.strftime('%d-%m-%Y')
            day=now.strptime(date,'%d-%m-%Y').weekday()
            time=now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dayName[day]},{date},{time}')


knownFaceEncodings=findEncodings(images)
print("Training image encoding completed...")

"""
    we have found the encodings for known training images
    now we need a face to match these encodings with
    and that face will come from our camera
"""
imageCapture=cv2.VideoCapture(0) # initializing web cameraand giving id as 0 in case of laptop webcam
                                        # and id as 1 in case of external camera
if not imageCapture.isOpened():
    print("Cannot open camera...")
    exit()
while True:
    success,img=imageCapture.read() # read image in real time frame by frame
    if not success:
        print("Cannot receive existing frame... ")
        break
    imgSmall=cv2.resize(img,(0,0),None,0.25,0.25) # reducing size of image by 1/4th (that is 0.5) for speeding the process
    imgSmall=cv2.cvtColor(imgSmall,cv2.COLOR_BGR2RGB) # convert image into RGB

    # now find encoding webcam images
    """
        we can find multiple faces in our webcam image
        so we need to find face location
        and send these loaction for finding encoding of current face in webcam
    """
    curFrameFaceLoc=face_recognition.face_locations(imgSmall) # find faces in current frame
    encodeCurFrameFace=face_recognition.face_encodings(imgSmall,curFrameFaceLoc) # fcaes in cam, current frame faces

# now to find face matching in current frame and face distance
    for encodeFace,faceLoc in zip(encodeCurFrameFace,curFrameFaceLoc):
        matches=face_recognition.compare_faces(knownFaceEncodings,encodeFace)
        faceDist=face_recognition.face_distance(knownFaceEncodings,encodeFace) # lowest distance will be best match
        #print(faceDist)
        matchIndex=np.argmin(faceDist) # give index of minimum value

        if matches[matchIndex]: # if face from camera are in directory
            name=imageName[matchIndex].upper()
            #print(name)
            y1,x2,y2,x1=faceLoc # assigning loactions of face sin current frame thta is in webcam
            y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255),2) # draw square around known faces
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,0,255),cv2.FILLED) # to show name 

            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markAttendence(name)
            
    cv2.imshow('Capturing Faces',img) # show original image, not small image that we resized
    if cv2.waitKey(1) & 0xFF==ord('x'):
        break
imageCapture.release()
cv2.destroyAllWindows()
print("\nAll attendence are marked correctly and stored in file..")
print("*********** LIST OF TODAY ATTENDEES ARE: ***********")
df=pd.read_csv("attend.csv")
print(df)
print("\n*** HERE IS ATTENDENCE SUMMARY ***\n")
print("Total number of students are: ",len(imageName))
print("Total attendees are: ",len(df))
print("total Absentees are: ",len(imageName)-len(df))


