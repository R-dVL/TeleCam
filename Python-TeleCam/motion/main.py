import RPi.GPIO as GPIO
from bot import *
from bot import motion_comment
import picamera

camera = picamera.PiCamera(resolution = "1920x1080")
camera.rotation = 180 # My PiCamera is rotated 180º.
camera.brightness = 60 # Dark house, had to increase brightness.

pir_input = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(pir_input, GPIO.IN)
GPIO.setwarnings(False)

def start_detection():
    pass

if __name__ == "__main__":
    start_detection()