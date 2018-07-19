import boto3
from picamera import PiCamera
import time
import datetime

camera = PiCamera()
def ClickPicture():
    date = "123"
    camera.resolution = (1024,768)
    camera.start_preview()

    time.sleep(1)

    image_name = date + '_img.jpg'

    camera.capture(image_name)
    camera.stop_preview()

   # GPIO.cleanup()

    return image_name

client = boto3.client('rekognition')

filename = ClickPicture()
with open(filename, 'rb') as image_file:
	image = image_file.read()
	response = client.detect_labels(Image = {'Bytes':image})
	print(response)

