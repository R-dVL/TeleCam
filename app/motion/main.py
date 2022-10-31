import random_reply
import time
import bot
import camera
from datetime import datetime
from .setup import *


def start_detection():
    while True:
        pir.wait_for_motion()  # Motion Start
        print("Detection.")
        filename = "{0:%Y}{0:%m}{0:%d}-{0:%H}{0:%M}{0:%S}".format(datetime.now())
        camera.capture("/home/rdvl/Documents/GitHub/TeleCam/data/photo/" + filename + ".jpg")
        bot.send_photo("/home/rdvl/Documents/GitHub/TeleCam/data/photo/" + filename + ".jpg")
        bot.send_message(random_reply.motion_comment())
        time.sleep(10)