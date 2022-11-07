import RPi.GPIO as GPIO 
import time 

GPIO.setwarnings(False)

ledPin = 11 
GPIO .setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, GPIO.HIGH) 

  

while True: 
GPIO. output (LedPin, PIO. HIGH) 
time.sleep(1) 
GPIO. output (LedPin, GPIO. Low)
time.sleep(1) 

 

GPIO.cleanup(); 