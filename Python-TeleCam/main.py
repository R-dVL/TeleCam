import bot
import threading


# Thread defined, used to call boy.py
class ThreadBot(threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      botstart()

Bot = ThreadBot(1, "Thread-1", 1)

if __name__ == '__main__':

   Bot.start()
   print("Pumuky despertando...") 
   message("Pumuky despertando...")
   message("Seleciona un modo con:\n/motion: sensor de movimiento.\n/stream: Cámara en directo.") 