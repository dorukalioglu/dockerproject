import OPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(7,GPIO.IN)
input = GPIO.input(7)
while True:
  if (GPIO.input(7)):
    print("Flame Detected")
  else:
    print("Not Detected")