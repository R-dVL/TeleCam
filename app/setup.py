import threading
import camera
import bot
import motion
import os
import glob

# Bot thread def
class Thread_1(threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
      
   def run(self):
      bot.start_bot()
      
BotThread = Thread_1(1, "Thread-1", 1)

# Streaming thread def
class Thread_2(threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
      
   def run(self):
      camera.start_streaming()

StreamThread = Thread_2(2, "Thread-2", 2)

# Motion Detection thread def
class Thread_3(threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
      
   def run(self):
      motion.start_detection()

MotionThread = Thread_3(3, "Thread-3", 3)

# Cleanup Data folder from previous session
files = glob.glob('/home/rdvl/Documents/GitHub/TeleCam/data/photo/*')
for f in files:
    os.remove(f)