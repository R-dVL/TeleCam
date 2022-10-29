import telegram
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import json
import config

# Setup
BotData = config.ConfigData

# Read data from JSON and use setters to assign Token and Chat ID
f = open("/home/rdvl/Documents/GitHub/TeleCam/config.json")
data = json.load(f)

for key, val in data["bot"].items():
    if key == "token":
        BotData.set(key, val)
            
    elif key == "chat":
        BotData.set(key, val)
            
f.close()

# Setup
ChatId = BotData.get("chat")
bot = telegram.Bot(token = BotData.get("token"))
updater = Updater(BotData.get("token"), use_context=True)