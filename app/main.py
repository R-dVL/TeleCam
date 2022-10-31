import random_reply
from setup import *

# Using module as script to start the program
if __name__ == '__main__':
   BotThread.start()  # Bot Thread start
   bot.send_message("Pumuky despertando...")
   print("Pumuky despertando...") 
   
   StreamThread.start()  # Livecamera Start
   print("Streaming active")
   bot.send_message(random_reply.stream_comment())
  
  # Motion detection Loop
   MotionThread.start()
   print("Motion detection active")