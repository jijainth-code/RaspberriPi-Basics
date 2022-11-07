import RPi.GPIO as GPIO 
import time 

GPIO.setwarnings(False)
ledPin= 11 

buttonPin = 16 
GPIO.setmode(GPIO.BOARD) 

 

GPIO.setup(ledPin, GPIO.OUT)
GPI0.output(ledPin, GPIO.LOW) 

 

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GP10 .PUD_UP)

 

while True: 
    GPIO.wait_for_edge (buttonPin, GPIO.Falling)
    print('Button Pressed')
    GPIO.output(ledPin, GPIO.HIGH) 
    GPIO.wait_for_edge(buttonPin, GPIO. RISING) 
    GP1O.output(ledPin, GPIO.LOW) 

GPIO.cleanup(); 