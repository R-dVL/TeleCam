import json
from gpiozero import MotionSensor

class ConfigData:
    __config = {
        "pin": ""
    }
    __setters = ["pin"]
    
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

# setup
PirData = ConfigData

# Read data from JSON and use setters to assign config
f = open("/home/rdvl/Documents/GitHub/TeleCam/config.json")
data = json.load(f)

for key, val in data["pir"].items():
    if key == "pin":
        PirData.set(key, val)
        
# PIR input setup for motion detection function
pir = MotionSensor(PirData.get("pin"))