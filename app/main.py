from gpiozero import MotionSensor
import time
import threading
import camera
import bot
import random_reply

# PIR input setup for motion detection function
pir = MotionSensor(4)

# Bot thread definition
class Thread_1(threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
      
   def run(self):
      bot.start_bot()
      
BotThread = Thread_1(1, "Thread-1", 1)

# Streaming thread definition
class Thread_2(threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
      
   def run(self):
      camera.start_streaming()

StreamThread = Thread_2(2, "Thread-2", 2)

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
      time.sleep(3)
      camera.capture("../data/photo/photo.jpg")
      bot.send_photo("../data/photo/photo.jpg")
      bot.send_message(random_reply.motion_comment())
      
      pir.wait_for_no_motion()  # Motion End
      print("Detection end.")
   