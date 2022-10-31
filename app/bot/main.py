from .setup import *
import camera
import random_reply

# Send picture method
def send_photo(path):
    bot.send_photo(ChatId, photo=open(path, 'rb'))
    
# Send message method
def send_message(text):
	bot.sendMessage(ChatId, text)

# Command to take a photo and send it back
def foto(update: Update, context: CallbackContext):
    camera.capture("/home/rdvl/Documents/GitHub/TeleCam/data/photo/photocmd.jpg")
    send_message(random_reply.photo_comment())
    send_photo("/home/rdvl/Documents/GitHub/TeleCam/data/photo/photocmd.jpg")

# I use this command just to know if the bot is running.
def start(update: Update, context: CallbackContext):
	update.message.reply_text("Er Puma al habla keskiere")

# Typical help function to output bot commands.
def help(update: Update, context: CallbackContext):
    update.message.reply_text("/foto: Me saco un selfie.\n/stream: 192.168.1.142:8000")
    
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