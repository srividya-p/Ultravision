from time import sleep
from gpiozero import PWMOutputDevice

MOTOR=14 #PIN 8
motor = PWMOutputDevice(14)

motor.value = 0.5
sleep(2)
motor.value = 0



