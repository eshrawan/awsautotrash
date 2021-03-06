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
object_sensor = 11
numberOfLabels = 10
objectDetected = False

def FindImageType(example):
    print("printing prediction")
    print(example)
    clas = classdictionary.class_dictionary()
    if example in clas:
        type = clas[example]
        print("Printing classified type by AWS")
        print(type)
        if type == "c":
            return("C")
        elif type == "r":
            return("R")
    else:
        return("N")

def RunMotor(typetry):
    if typetry == "c":
        print("wet waste detected. Motor is turning clockwise")
        pwm=GPIO.PWM(12,100)
        GPIO.output(motor_signal1,GPIO.HIGH)
        GPIO.output(motor_signal2,GPIO.LOW)
        pwm.start(70)
        sleep(10)
        pwm.stop()
    else:
        pwm=GPIO.PWM(12,100)
        print("recyclabe waste detected. Motor turning counter-clockwise")
        GPIO.output(motor_signal1,GPIO.LOW)
        GPIO.output(motor_signal2,GPIO.HIGH)
        pwm.start(70)
        sleep(10)
        pwm.stop()
    print("Ready for next item.")
    GPIO.cleanup()


def RunServo():
    p = GPIO.PWM(servo_signal, 50)
    p.start(7.5)
    try:
        print("reject waste is detected. Running servo")
        p.ChangeDutyCycle(7.5)
        p.ChangeDutyCycle(2.5)
        p.ChangeDutyCycle(12.5)
        print("Ready for next item.")
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
    print("Image is taken.Saving")
    camera.stop_preview()

    return image_name

client = boto3.client('rekognition')
def MasterFunction():
    numberOfR = 0
    numberOfC = 0
    numberOfN = 0
    filename = ClickPicture()
    with open(filename, 'rb') as image_file:
        image = image_file.read()
        print("Connecting to AWS Rekognition")
        response = client.detect_labels(Image = {'Bytes':image})
        list_of_response = response["Labels"]
        image_types = []
        for label in list_of_response[:numberOfLabels]:
            top_response = label["Name"]
            if label["Confidence"] >= 70.0:
                 trashCategory = FindImageType(top_response.lower())
                 if trashCategory == "C":
                     numberOfC = numberOfC+1
                 elif trashCategory == "R":
                     numberOfR = numberOfR+1
                 else:
                     numberOfN = numberOfN+1
        if numberOfR > numberOfC and numberOfR > numberOfN:
            RunMotor("r")
        elif numberOfC > numberOfR and numberOfC > numberOfN:
            RunMotor("c")
        else:
            RunServo()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(object_sensor, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(servo_signal, GPIO.OUT)
GPIO.setup(motor_signal1, GPIO.OUT)
GPIO.setup(motor_signal2, GPIO.OUT)

while True:

    object_sensor_state_first = GPIO.input(object_sensor)
    time.sleep(0.05)
    object_sensor_state_second = GPIO.input(object_sensor)

    object_sensor_state = 0 #default state
    if object_sensor_state_first == object_sensor_state_second:
        object_sensor_state = object_sensor_state_first
    object_sensor_state = 1
    if object_sensor_state == 1 and objectDetected == False:
        objectDetected = True
        MasterFunction()
    elif object_sensor_state == 0:
        objectDetected= False
