import RPi.GPIO as GPIO 
import time 

 

buttonPin = 16 
GP1O.setmode(GPIO.BOARO) 

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) 

while True:
Anput_state = GPIO. input (buttorPin)
if input_state == False:
    print("Button Pressed") 
    time.sleep(0.3) #viait f
   

GPIO.cleanup(); 
