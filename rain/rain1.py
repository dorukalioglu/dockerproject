from time import sleep
import os
import OPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
state = GPIO.input(23)

if (state == 0):
    print ("Water detected!")
else:
    print ("Water not detected")
sleep(10)