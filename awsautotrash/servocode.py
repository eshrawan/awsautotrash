import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 20)

p.start(7.5)

try:
    while True:
        p.ChangeDutyCycle(5.5)  # turn towards 90 degree
        time.sleep(2) # sleep 1 second
        p.ChangeDutyCycle(2.5)  # turn towards 0 degree
        time.sleep(2) # sleep 1 second 
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
