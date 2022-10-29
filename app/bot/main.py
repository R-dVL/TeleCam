import telegram
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from .setup import *
import camera
import random_reply

# Setup
ChatId = BotData.get("chat")
bot = telegram.Bot(token = BotData.get("token"))
updater = Updater(BotData.get("token"), use_context=True)

# Sends a picture, used in motion.py.
def send_photo(path):
    bot.send_photo(ChatId, photo=open(path, 'rb'))
    
# Function to just send a message (defined in "text" when the function is called).
def send_message(text):
	bot.sendMessage(ChatId, text)

# Command to take a photo
def foto(update: Update, context: CallbackContext):
    camera.capture("/home/rdvl/Documents/GitHub/Python-TeleCam/data/photo/photocmd.jpg")
    bot.send_message(random_reply.photo_comment())
    bot.send_photo("/home/rdvl/Documents/GitHub/Python-TeleCam/data/photo/photocmd.jpg")
    
    
# I use this command just to know if the bot is running.
def start(update: Update, context: CallbackContext):
	update.message.reply_text("Er Puma al habla keskiere")

# Typical help function to output bot commands.
def help(update: Update, context: CallbackContext):
    update.message.reply_text("/video: Te paso mi último clip.\n/foto: Me saco un selfie.\n/motion: Inicio sensor de movimiento.\n/stream: Arranco streaming: 192.168.1.142:8000")
    
# Response to unknown commands (filters every /"text" introduced in the chat).
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Que es'%s', no entiendo wasajasa" % update.message.text)

# Response to commands introduced in chat.
def start_bot():
    updater.dispatcher.add_handler(CommandHandler('foto', foto))
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
    updater.start_polling()

if __name__=='__main__':
    start_bot()
