import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

BUZZER=16
GPIO.setup(BUZZER, GPIO.OUT)

for _ in range(5):
    GPIO.output(BUZZER,GPIO.HIGH)
    print ("Beep")
    sleep(0.7) # Delay in seconds
    GPIO.output(BUZZER,GPIO.LOW)
    print ("No Beep")
    sleep(0.7)
    
for _ in range(5):
    GPIO.output(BUZZER,GPIO.HIGH)
    print ("Beep")
    sleep(0.5) # Delay in seconds
    GPIO.output(BUZZER,GPIO.LOW)
    print ("No Beep")
    sleep(0.5)
    
for _ in range(5):
    GPIO.output(BUZZER,GPIO.HIGH)
    print ("Beep")
    sleep(0.2) # Delay in seconds
    GPIO.output(BUZZER,GPIO.LOW)
    print ("No Beep")
    sleep(0.2)