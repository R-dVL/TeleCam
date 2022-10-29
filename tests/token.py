import json

f = open("/home/rdvl/Documents/GitHub/Python-TeleCam/data/config/config.json")
data = json.load(f)

for key, val in data["bot"].items():
    print(val)