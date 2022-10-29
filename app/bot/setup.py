import telegram
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import json

# These methods are created in order to protect the token and chat ID of the bot
class ConfigData:
    __config = {
        "token": "",
        "chat": "",
    }
    __setters = ["token", "chat"]
    
    # Getter method
    @staticmethod
    def get(name):
        return ConfigData.__config[name]
    
    # Setter method
    @staticmethod
    def set(name, value):
        if name in ConfigData.__setters:
            ConfigData.__config[name] = value
        else:
            raise NameError("Not accepted configuration.")
        
# Setup
BotData = ConfigData

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