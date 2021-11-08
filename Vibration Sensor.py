import RPi.GPIO as GPIO
import time as time
import LED                      #importing LED script

#setting up GPIO 
channel = 17                    #change to correct number pls
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)


def vibrationFound(channel):
    if GPIO.input(channel):
        callFunctionHere = 0     #call LED light-up function     


GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300) #lets us know when pin goes HIGH or LOW
GPIO.add_event_callback(channel, vibrationFound)          #assigns function to GPIO PIN, runs function on change

#infinite loop
while True: 
        time.sleep(1)