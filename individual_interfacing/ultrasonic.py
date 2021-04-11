import RPi.GPIO as GPIO
import time

#Use mode BOARD(Pin numbers) or BCM(GPIO numbers)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 23 #PIN 16
ECHO = 24 #PIN 18

print("Setting Trigger and Echo Pins...")

#Set Trigger as Output Pin
GPIO.setup(TRIG, GPIO.OUT)
#Set Echo as Input Pin
GPIO.setup(ECHO, GPIO.IN)

#Ensure that Trigger is set to low initially and let sensor settle.
GPIO.output(TRIG, False) 
print("Waiting For Sensor To Settle")
time.sleep(2)

#Set Trigger to high for a duration of 10 microseconds.
#This pulse tells the module to start sending Ultrasonic Bursts (8 bursts of 40 kHZ)
GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

#Store the start time of the pulse
while GPIO.input(ECHO)==0:
    pulse_start = time.time()
   
#Store the end time of the pulse
while GPIO.input(ECHO)==1:
    pulse_end = time.time()

#Calculate difference = The time taken for pulse to hit obstacle and come back.
pulse_duration = pulse_end - pulse_start
#Distance = Speed * (Time/2)
#Assume speed of sound as 34300 cm/s
distance = pulse_duration * 17150
distance = round(distance, 2)
print("Measured Distance =", distance)    

