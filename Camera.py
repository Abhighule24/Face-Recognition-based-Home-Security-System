import time
import datetime
import cv2
import threading
#import cv2.cv as cv
import config
import picamera
import Mail
import Buzz

def detect_faces(image):
    haar_faces = cv2.CascadeClassifier(config.HAAR_FACES)
    detected = haar_faces.detectMultiScale(image, scaleFactor=config.HAAR_SCALE_FACTOR, 
                minNeighbors=config.HAAR_MIN_NEIGHBORS, 
                minSize=config.HAAR_MIN_SIZE, 
                flags=cv2.CASCADE_SCALE_IMAGE)
    
    return detected

def Capture():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    ts=time.time()
    font = cv2.FONT_HERSHEY_SIMPLEX
    id = 0

    # names related to ids: example ==> Marcelo: id=1,  etc
    names = ['None','ABHISHEK', 'VIRAL'] 

    dt= datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    with picamera.PiCamera() as camera:
            camera.capture("CapImg/"+dt+".png") 
    image = cv2.imread("CapImg/"+dt+".png")
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = detect_faces(image)
    if len(faces) != 0:
        for (x,y,w,h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), 255)
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

            # Check if confidence is less them 100 ==> "0" is perfect match 
            if (confidence < 100):
                id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
            else:
                id = "UNKNOWN PERSON"
                confidence = "  {0}%".format(round(100 - confidence))
        
            cv2.putText(image, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            #cv2.putText(image, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
            
        cv2.imwrite("DetectImg/"+dt+".png", image)
        print("FACE DETECTED AND RECOGNISED")
        Buzz.FDB()
        thm=threading.Thread(Mail.FDSendMail(dt,id))
        thm.start()
        ths=threading.Thread(Showimg(image))
        ths.start()
    else:
        print('NO FACE DETECTED')
        Buzz.NFDB()
        thm=threading.Thread(Mail.NFDSendMail(dt))
        thm.start()
        ths=threading.Thread(Showimg(image))
        ths.start()
    with open("Gallery.txt",'a') as f:
            f.write("CapImg/%s.png\n"%dt)
    
def Showimg(image):
    cv2.destroyAllWindows()
    cv2.namedWindow('INTRUDER',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('INTRUDER',300,480)
    cv2.imshow('INTRUDER', image)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
