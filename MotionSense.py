import RPi.GPIO as GPIO
import time
import threading
import Camera
import IoT
def Motion():
    try:
        while True:
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(7, GPIO.IN)
            time.sleep(0.5) # to stabilize sensor
            print("WAITING FOR MOTION DETECTION")
            if GPIO.input(7):
                print("MOTION DETECTED...")
                thc=threading.Thread(Camera.Capture())
                thc.start()
                time.sleep(0.5) #to avoid multiple detection
            else:
                pass
    except KeyboardInterrupt:
        IoT.Enter()

