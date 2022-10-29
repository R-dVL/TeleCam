import json
import config

# Setup
BotData = config.ConfigData

f = open("/home/rdvl/Documents/GitHub/Python-TeleCam/app/config/config.json")
data = json.load(f)

for key, val in data["bot"].items():
    if key == "token":
        BotData.set(key, val)
            
    elif key == "chat":
        BotData.set(key, val)
            
f.close()