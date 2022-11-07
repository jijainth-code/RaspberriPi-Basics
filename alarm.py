import RPi.GPIO as GPIO
import time 

GPIO.setwarnings (False)
pirPin=7 # ted t

buzzerPin = 11 # is connected to the + i ve connect
GPIO.setmode(GPIO.BOARD) # Nunt PI phy ti

 

 

 

GPIO.setup(pirPin, GPIO.IN) 
GPIO.setup(buzzerPin, GPIO.OUT)
GPIO.output(buzzerPin, GPIO.LOW)

 

def soundAlarm(pirPin) :

    print ("Sound Alarm")
    GPIO.output(buzzerPin, GPIO.HIGH) #
    time.sleep(2) # 4

    turnOffAlarm(pirPin) #

def turn0ffAlarm(pirPin) :

    GP1O.output(buzzerPin, GPIO.LOW) #


GPIO.add_event_detect(pirPin, GPIO.RISING, callback=soundAlarm!)

 
