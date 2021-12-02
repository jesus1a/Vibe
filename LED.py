#So far this should just turn an LED on and off constantly in 5 sec intervals
import RPi.GPIO as GPIO
import time as time

def blink(led_pin):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led_pin,GPIO.OUT)
    x = 0

    while(x < 10):
        GPIO.output(led_pin,GPIO.HIGH)
        time.sleep(.5)
        GPIO.output(led_pin,GPIO.LOW)
        time.sleep(.5)
        x+=1
