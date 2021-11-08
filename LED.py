#So far this should just turn an LED on and off constantly in 5 sec intervals
import RPi.GPIO as GPIO
import time as time

led_pin = 17 #port num will change on finall realese

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin,GPIO.OUT)

def on():
    GPIO.output(led_pin,GPIO.HIGH)
def off():
    GPIO.output(led_pin,GPIO.LOW)

GPIO.cleanup()
