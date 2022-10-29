import json

f = open("config.json")
data = json.load(f)

for key, val in data["bot"].items():
    print(val)