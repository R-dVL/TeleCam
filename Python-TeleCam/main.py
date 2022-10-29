import bot
import threading


# Thread defined, used to call boy.py
class Thread_1(threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
      
   def run(self):
      bot.start_bot()

BotThread = Thread_1(1, "Thread-1", 1)

if __name__ == '__main__':

   BotThread.start()
   print("Pumuky despertando...") 
   bot.send_message("Pumuky despertando...")
   bot.send_message("Seleciona un modo con:\n/motion: sensor de movimiento.\n/stream: Cámara en directo.") 