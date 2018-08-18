import boto3
from picamera import PiCamera
import time
import datetime
import l293d.driver as l293d
import RPi.GPIO as GPIO
from time import sleep
from awsautotrash import class_dictionary

def FindImageType(example):
    if example in class_dictionary:
        type = class_dictionary[example]
        if type == "c":
            RunMotor("c")
            return("C")
        elif type == "r":
            RunMotor("r")
            return("R")
    else:
        RunServo()
        return("N")

def RunMotor(typetry):

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)
    if typetry == "c":
        print("turning clockwise")
        GPIO.output(16,GPIO.HIGH)
        GPIO.output(18,GPIO.LOW)
        GPIO.output(22,GPIO.HIGH)
    else:
        print("turning counter-clockwise")
        GPIO.output(16,GPIO.LOW)
        GPIO.output(18,GPIO.HIGH)
        GPIO.output(22,GPIO.HIGH)
    GPIO.cleanup()


def RunServo():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    p = GPIO.PWM(12, 50)
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

def MasterFunction():
    client = boto3.client('rekognition')
    filename = ClickPicture()
    with open(filename, 'rb') as image_file:
        image = image_file.read()
        response = client.detect_labels(Image = {'Bytes':image})
        top_response = response[0]
        FindImageType(top_response)

while True:
    MasterFunction()
