import os
import time
from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep


channel = port.PA18
gpio.init()
gpio.setcfg(channel, gpio.INPUT)
sign = 0
space_start = 0
space_end = 0
space = 0
pulse = 0
try:
	os.system("clear"); 
	print ("Press CTRL+C to exit")
	
	while True:
		
		while gpio.input(channel)==1:
			pulse = 0
			space_end = time.time()
			
		while gpio.input(channel)==0:
			pulse = pulse + 1
			space_start = time.time()
		sleep(0.5)
		print (pulse)
		space_duration = (space_start - space_end) *100000
		print (space_duration)
		
except KeyboardInterrupt:
	print ("Bitti.")
	
