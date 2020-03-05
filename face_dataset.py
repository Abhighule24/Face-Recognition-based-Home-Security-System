import cv2
import os
import config
#face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
def detect_faces(image):
    haar_faces = cv2.CascadeClassifier(config.HAAR_FACES)
    detected = haar_faces.detectMultiScale(image, scaleFactor=config.HAAR_SCALE_FACTOR, 
                minNeighbors=config.HAAR_MIN_NEIGHBORS, 
                minSize=config.HAAR_MIN_SIZE, 
                flags=cv2.CASCADE_SCALE_IMAGE)
    
    return detected
cam = cv2.VideoCapture(0)
#cam.set(3, 640) # set video width
#cam.set(4, 480) # set video height



# For each person, enter one numeric face id
face_id = input('\n enter user id end press <return> ==>  ')

print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
count = 0
i=0
while i<=1:

    ret, img = cam.read()
    #img = cv2.flip(img, -1) # flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detect_faces(img)
    cv2.imshow("image",img)
    if len(faces) != 0:
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)

        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
    
    i=i+1

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
#cv2.destroyAllWindows()
