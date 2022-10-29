import config
import json

BotData = config.ConfigData

f = open("config.json")
data = json.load(f)

for key, val in data["bot"].items():
    if key == "token":
        BotData.set(key, val)
        
    if key == "chat":
        BotData.set(key, val)