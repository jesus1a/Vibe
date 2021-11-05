import RPi.GPIO as GPIO
import time as time
GPIO.cleanup()
led_pin = 4
def initialize():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led_pin,GPIO.OUT)

def main():
    while True:
        GPIO.output(led_pin,GPIO.HIGH)
        time.sleep(5000)
        GPIO.output(led_pin,GPIO.LOW)

initialize()
main()
GPIO.cleanup()
