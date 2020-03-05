import RPi.GPIO as GPIO
import time
def NFDB():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(23, GPIO.OUT) #BUzzer
    GPIO.output(23, GPIO.HIGH)
    time.sleep(5) #Buzzer turns on for 0.5 sec
    GPIO.output(23, GPIO.LOW)
    GPIO.cleanup()
def FDB():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(23, GPIO.OUT) #BUzzer
    GPIO.output(23, GPIO.HIGH)
    time.sleep(1) #Buzzer turns on for 0.5 sec
    GPIO.output(23, GPIO.LOW)
    GPIO.cleanup()
    
