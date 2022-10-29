import threading
import camera
import bot
from gpiozero import MotionSensor

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