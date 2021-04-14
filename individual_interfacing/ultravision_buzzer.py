import RPi.GPIO as GPIO
import time

#Use mode BOARD(Pin numbers) or BCM(GPIO numbers)
GPIO.setmode(GPIO.BCM)
#Set GPIO Warnings to False
GPIO.setwarnings(False)

TRIG = 23 #PIN 16
ECHO = 24 #PIN 18
BUZZER = 16 #PIN 36

print("Setting Trigger, Echo and Buzzer Pins...")

#Set Trigger as Output Pin
GPIO.setup(TRIG, GPIO.OUT)
#Set Echo as Input Pin
GPIO.setup(ECHO, GPIO.IN)
#Set Buzzer as Output Pin
GPIO.setup(BUZZER, GPIO.OUT)

#Ensure that Trigger is set to low initially and let sensor settle.
GPIO.output(TRIG, False) 
print("Waiting For Sensor To Settle...")
time.sleep(2)
#Ensure that Buzzer is set to low initially
GPIO.output(BUZZER, False)

def current_distance():
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
    return distance

def beep_frequency(distance):
    # If the distance is bigger than 50cm, do not beep.
    if distance > 50:
        return -1
    # If the distance is between 50 and 30 cm, beep once a second.
    elif distance <= 50 and distance >=30:
        return 1
    # If the distance is between 30 and 20 cm, beep twice a second.
    elif distance < 30 and distance >= 20:
        return 0.5
    # If the distance is between 20 and 10 cm, beep four times a second.
    elif distance < 20 and distance >= 10:
        return 0.25
    # If the distance is smaller than 10 cm, beep constantly.
    else:
        return 0
    
def main():
    try:
        #Keep Running till the program is ended by the user.
        while True:
            #Get Current Distance
            distance = current_distance()
            print("Distance =", distance)
            #Get Frequency for that distance
            freq = beep_frequency(distance)
            #No Beeping Edge Case #1
            if(freq == -1):
                GPIO.output(BUZZER, False)
                time.sleep(0.25)
            #Continuous Beeping Edge Case #2
            elif(freq == 0):
                GPIO.output(BUZZER, True)
                time.sleep(0.25)
            else:
                GPIO.output(BUZZER, True)
                time.sleep(0.2) #Start beep for 0.2 seconds on entering any range
                GPIO.output(BUZZER, False)
                time.sleep(freq) #Beep according to returned frequency
    except KeyboardInterrupt:
        #Set Buzzer output to False and Clean up GPIOs
        GPIO.output(BUZZER, False)
        GPIO.cleanup()
        print("Terminated.")

if __name__ == "__main__":
    main()




