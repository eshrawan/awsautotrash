import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(18, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

def clockwise():
        GPIO.output(18,GPIO.HIGH)
        GPIO.output(16,GPIO.LOW)

def anticlockwise():
        GPIO.output(18,GPIO.LOW)
        GPIO.output(16,GPIO.HIGH)

pwm=GPIO.PWM(12,100)
anticlockwise()
pwm.start(70)
sleep(5)
pwm.stop()
GPIO.cleanup()
exit()
