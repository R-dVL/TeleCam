from gpiozero import MotionSensor
import time
import threading
import camera
import bot
import random_reply

pir = MotionSensor(4)

# Thread defined, used to call boy.py
class Thread_1(threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
      
   def run(self):
      bot.start_bot()
      
class Thread_2(threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
      
   def run(self):
      camera.start_streaming()

BotThread = Thread_1(1, "Thread-1", 1)
StreamThread = Thread_2(2, "Thread-2", 2)

if __name__ == '__main__':
   BotThread.start()
   print("Pumuky despertando...") 
   
   StreamThread.start()
   print("Streaming activo")
   bot.send_message(random_reply.stream_comment())
  
   while True:
      pir.wait_for_motion()  # Motion Start
      print("Detection.")
      time.sleep(3)
      camera.capture("../data/photo/photo.jpg")
      bot.send_photo("../data/photo/photo.jpg")
      bot.send_message(random_reply.motion_comment())
      
      pir.wait_for_no_motion()  # Motion End
      print("Detection end.")
   