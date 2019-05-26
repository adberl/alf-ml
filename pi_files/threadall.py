#from keras.models import Sequential
#from keras.models import model_from_json
#from keras.layers import Dense

import numpy as np
import threading
import time
import RPi.GPIO as GPIO


#loading model
"""
json_file = open('keras/model.json', 'r')
model = json_file.read()
json_file.close()

model = model_from_json(model)

model.load_weights('keras/model.h5')
"""
#loading model done

#setting up GPIO

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 21
GPIO_ECHO = 20

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

chan_list = [4, 13, 17, 22, 26, 27]
GPIO.setup(chan_list, GPIO.IN, pull_up_down=GPIO.PUD_UP)

outpin_list = [18, 24, 25, 12]
GPIO.setup(outpin_list, GPIO.OUT)

dist = 0.0

def distance():
    global dist
    while True:
        # set Trigger to HIGH
        GPIO.output(GPIO_TRIGGER, True)

        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)

        StartTime = time.time()
        StopTime = time.time()

        # save StartTime
        print("w1")
        while GPIO.input(GPIO_ECHO) == 0:
            StartTime = time.time()

        print("w2")
        # save time of arrival
        while GPIO.input(GPIO_ECHO) == 1:
            StopTime = time.time()

        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        dist = (TimeElapsed * 34300) / 2
        time.sleep(0.5)
#        print("distance measured", dist)
#        time.sleep(1)

threading.Thread(target=distance).start()

while True:
    print(dist)
"""    if dist > 7.0:
        # Follow line
        print("following line %.1f" % dist)
        GPIO.output([12, 24], GPIO.HIGH)
        GPIO.output([18, 25], GPIO.LOW)
    else:
        print("avoiding obstacle %.1f" % dist)
        rotate_time = 1
        drive_time = 2
        #rotate
        GPIO.output([18, 25, 12], GPIO.LOW)
        GPIO.output(24, GPIO.HIGH)
        time.sleep(rotate_time)
        #go forwards
        GPIO.output([12, 24], GPIO.HIGH)
        time.sleep(drive_time)
        #rotate back
        GPIO.output([18, 25, 12], GPIO.LOW)
        GPIO.output(12, GPIO.HIGH)
        time.sleep(rotate_time)
        #drive back
        GPIO.output([12, 24], GPIO.HIGH)
        time.sleep(drive_time * 2)
        #rotate again
        GPIO.output([18, 25, 12], GPIO.LOW)
        GPIO.output(12, GPIO.HIGH)
        time.sleep(rotate_time)
        # drive back on track
        GPIO.output([12, 24], GPIO.HIGH)
        time.sleep(drive_time)
        # rotate on track
        GPIO.output([18, 25, 12], GPIO.LOW)
        GPIO.output(24, GPIO.HIGH)
        time.sleep(rotate_time)
"""
