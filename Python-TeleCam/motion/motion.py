import RPi.GPIO as GPIO
from bot import *
from randreply import RandMotion
import picamera

camera = picamera.PiCamera(resolution = "1920x1080")
camera.rotation = 180 # My PiCamera is rotated 180º.
camera.brightness = 60 # Dark house, had to increase brightness.

pir_input = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(pir_input, GPIO.IN)
GPIO.setwarnings(False)

def start_detection():
    shot = 0
    i = 0

    while True:

        print(GPIO.input(pir_input))

        if GPIO.input(pir_input):
            camera.capture('/home/rdvl/GatiCam/motion_feed/puma'+str(i)+'.jpg')
            i += 1
            shot += 1

        if GPIO.input(pir_input) and shot == 7:
            camera.capture('/home/rdvl/GatiCam/lastmotion/lastpuma.jpg') # Once the motion is stable, notifies via telegram and sends a pic.
            sendphoto('/home/rdvl/GatiCam/lastmotion/lastpuma.jpg')
            message(RandMotion())
            print("Algo detectado")

        if i == 100:
            i = 0

        if not GPIO.input(pir_input):
            shot = 0

        if mode["photo"] == True:
            camera.capture('/home/rdvl/GatiCam/lastmotion/photo.jpg')
            bot.send_photo(CHAT_ID, photo=open('/home/rdvl/GatiCam/lastmotion/photo.jpg', 'rb'))
            mode["photo"] = False
            bot.send_message(CHAT_ID, RandFoto())

if __name__ == "__main__":
    start_detection()