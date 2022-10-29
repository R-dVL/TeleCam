import telegram
import config
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from makevideo import make_video
from randreply import RandStream, RandFoto, RandVideo

ChatId = botdata.get("chat")
bot = telegram.Bot(token = botdata.get("token"))
updater = Updater(TOKEN, use_context=True)

mode = {"motion" : False, "stream": False, "photo" : False}

# Sends a picture, used in motion.py.
def send_photo(path):
    bot.send_photo(ChatId, photo=open(path, 'rb'))
    
# Function to just send a message (defined in "text" when the function is called).
def send_message(text):
	bot.sendMessage(ChatId, text)

# This command will make a video with motion_feed jpg's and send it.
def send_video(update: Update, context: CallbackContext):
    make_video()
    bot.send_document(ChatId, document=open(botdata.get("video"), "rb"))
    bot.send_message(ChatId, RandVideo())

# Starts motion thread in main.py
def mode_motion(update: Update, context: CallbackContext):
    mode["stream"] = False
    mode["motion"] = True

# Starts streaming thread in main.py
def mode_stream(update: Update, context: CallbackContext):
    mode["motion"] = False
    mode["stream"] = True
    bot.send_message(ChatId, RandStream())

# Takes a photo, have to test it
def mode_foto(update: Update, context: CallbackContext):
    mode["photo"] = True
    
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
    updater.dispatcher.add_handler(CommandHandler('video', video))
    updater.dispatcher.add_handler(CommandHandler('motion', motion))
    updater.dispatcher.add_handler(CommandHandler('stream', stream))
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
    updater.start_polling()

if __name__=='__main__':
    start_bot()
