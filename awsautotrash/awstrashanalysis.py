import boto3
from picamera import PiCamera
import time
import datetime
import l293d.driver as l293d
import RPi.GPIO as GPIO
from time import sleep
import classdictionary
servo_signal = 12
motor_signal1 = 18
motor_signal2 = 16
motor_signal3 = 22
object_sensor = 11

def FindImageType(example):
    print(example)
    clas = classdictionary.class_dictionary()
    if example in clas:
        type = clas[example]
        print(type)
        if type == "c":
            #RunMotor("c")
            return("C")
        elif type == "r":
            #RunMotor("r")
            return("R")
    else:
        #RunServo()
        return("N")

def RunMotor(typetry):
    if typetry == "c":
        print("turning clockwise")
        GPIO.output(motor_signal2,GPIO.HIGH)
        GPIO.output(motor_signal1,GPIO.LOW)
        GPIO.output(motor_signal3,GPIO.HIGH)
    else:
        print("turning counter-clockwise")
        GPIO.output(motor_signal2,GPIO.LOW)
        GPIO.output(motor_signal1,GPIO.HIGH)
        GPIO.output(motor_signal3,GPIO.HIGH)
    GPIO.cleanup()


def RunServo():
    p = GPIO.PWM(servo_signal, 50)
    p.start(7.5)
    try:
        print("running servo")
        p.ChangeDutyCycle(7.5)
        p.ChangeDutyCycle(2.5)
        p.ChangeDutyCycle(12.5)
    except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()

camera = PiCamera()
def ClickPicture():
    date = "123"
    camera.resolution = (1024,768)
    camera.start_preview()
    time.sleep(1)
    image_name = date + '_img.jpg'
    camera.capture(image_name)
    camera.stop_preview()

    return image_name

client = boto3.client('rekognition')
def MasterFunction():
    filename = ClickPicture()
    with open(filename, 'rb') as image_file:
        image = image_file.read()
        response = client.detect_labels(Image = {'Bytes':image})
        list_of_response = response["Labels"]
        image_types = []
        for label in list_of_response[:3]:
        	print(label["Name"])
        	top_response = label["Name"]
        	a = FindImageType(top_response.lower())
        	image_types.append(a)
        print(image_types)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(object_sensor, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(servo_signal, GPIO.OUT)
GPIO.setup(motor_signal1, GPIO.OUT)
GPIO.setup(motor_signal2, GPIO.OUT)
GPIO.setup(motor_signal3, GPIO.OUT)

#while True:
    #object_sensor_state = GPIO.input(object_sensor)
    #if object_sensor_state == 1:
        #MasterFunction()
object_sensor_state = GPIO.input(object_sensor)
if object_sensor_state == 1:
	MasterFunction()
