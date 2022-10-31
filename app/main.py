import time
import random_reply
from setup import *
from gpiozero import MotionSensor

# PIR input setup for motion detection function
pir = MotionSensor(4)

# Using module as script to start the program
if __name__ == '__main__':
   BotThread.start()  # Bot Thread start
   bot.send_message("Pumuky despertando...")
   print("Pumuky despertando...") 
   
   StreamThread.start()  # Livecamera Start
   print("Streaming activo")
   bot.send_message(random_reply.stream_comment())
  
  # Motion detection Loop
   while True:
      pir.wait_for_motion()  # Motion Start
      print("Detection.")
      camera.capture("/home/rdvl/Documents/GitHub/TeleCam/data/photo/photo.jpg")
      bot.send_photo("/home/rdvl/Documents/GitHub/TeleCam/data/photo/photo.jpg")
      bot.send_message(random_reply.motion_comment())
      
      pir.wait_for_no_motion()  # Motion End
      print("Detection end.")
   