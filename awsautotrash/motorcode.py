#enables change in two direcitons
#import l293d.driver as l293d
# Motor 1 uses Pin 22, Pin 18, Pin 16
#motor1 = l293d.motor(22,18,16)
# Run the motors so visible
#for i in range(0,150):
  #motor1.clockwise()
#293d.cleanup()

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

# Setting relay pins as output
#GPIO.setup(18, GPIO.OUT)

#while (True):
 
    # Turning relay ON
    #GPIO.output(18, GPIO.HIGH)
    # Sleep for 5 seconds
    #sleep(0.5)
    # Turning relay OFF
    #GPIO.output(18, GPIO.LOW)
    # Sleep for 5 seconds
    #sleep(0.5)
#GPIO.cleanup()

GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.output(23, GPIO.HIGH)

def forward():
	GPIO.output(19, GPIO.HIGH)
	sleep(2)
	GPIO.output(19, GPIO.LOW)

def reverse():
	GPIO.output(21, GPIO.HIGH)
	sleep(2)
	GPIO.output(21, GPIO.LOW)

while True:
	forward()
	sleep(1)
	reverse()
