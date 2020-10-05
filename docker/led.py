#!/usr/bin/env python
"""Basic blinking led example.

The led on A20-OLinuXino-MICRO  blinks with rate of 1Hz like "heartbeat".
"""

import os
import sys

if not os.getegid() == 0:
    sys.exit('calisti')


from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port

led = port.PA18
gpio.init()
gpio.setcfg(led, gpio.OUTPUT)


try:
    print ("Press CTRL+C to exit")
    while True:
        gpio.output(led, 0)
        sleep(0.1)
        gpio.output(led, 1)
        sleep(0.1)
        sleep(0.6)

except KeyboardInterrupt:
	gpio.output(led,0)
	print ("Bitti.")
