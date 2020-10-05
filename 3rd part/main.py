import OPi.GPIO as GPIO
import dht11
import time
import datetime
from pyA20.gpio import gpio
from pyA20.gpio import port
PIN2 = port.PG6
gpio.init()
#gpio.cleanup()
instance = dht11.DHT11(pin=PIN2)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(14, GPIO.IN)         #Read output from Gas sensor
GPIO.setup(13, GPIO.IN)         #Read output from Gas sensor
GPIO.setup(12, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(3, GPIO.OUT)         #LED output pin
try:
    while True:
        result = instance.read()
		if result.is_valid():
			print("Last valid input: " + str(datetime.datetime.now()))
			print("Temperature: %d C" % result.temperature)
			print("Humidity: %d %%" % result.humidity)
        
        flame=GPIO.input(11)
        gas=GPIO.input(12)
        motion=GPIO.input(13)
        rain=GPIO.input(14)
        if flame==0:                 #When output from motion sensor is LOW
            print ("No Flame",flame)

        elif flame==1:               #When output from motion sensor is HIGH
            print ("Flame detected",flame)
        if gas==0:
            print ("No gas",gas)
        elif gas==1:
            print ("Gas detected", gas)
        if motion==0:                 #When output from motion sensor is LOW
            print ("No Flame",motion)

        elif motion==1:               #When output from motion sensor is HIGH
            print ("Flame detected",motion  )  
        if rain==0:                 #When output from motion sensor is LOW
            print ("No Flame",rain)

        elif rain==1:               #When output from motion sensor is HIGH
            print ("Flame detected",rain   )    
        time.sleep(0.5)
except KeyboardInterrupt:
	print ("Bye.")