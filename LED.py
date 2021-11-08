#So far this should just turn an LED on and off constantly in 5 sec intervals
import RPi.GPIO as GPIO
import time as time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.OUT)


def blink(detect, pin):
    led_pin = pin
    while(detect):
        GPIO.output(led_pin,GPIO.HIGH)
        time.sleep(.5)
        GPIO.output(led_pin,GPIO.LOW)
        time.sleep(.5)

GPIO.cleanup()
