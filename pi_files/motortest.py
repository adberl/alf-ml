import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

outpin_list = [18, 24, 25, 12]
GPIO.setup(outpin_list, GPIO.OUT)

while True:
    GPIO.output([18, 25, 12], GPIO.LOW)
    GPIO.output(24, GPIO.HIGH)
    time.sleep(3)
    GPIO.output([18, 25, 24], GPIO.LOW)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(3)

GPIO.cleanup()
