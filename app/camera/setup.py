import picamera
import pyshine as ps
import json

# These methods are created in order to protect the token and chat ID of the bot
class ConfigData:
    __config = {
        "resolution": "",
        "framerate": "",
        "rotation": "",
        "brightness": "",
    }
    __setters = ["resolution", "framerate", "rotation", "brightness"]
    
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
CamData = ConfigData

# Read data from JSON and use setters to assign config
f = open("/home/rdvl/Documents/GitHub/TeleCam/config.json")
data = json.load(f)

for key, val in data["camera"].items():
    if key == "resolution":
        CamData.set(key, val)
            
    elif key == "framerate":
        CamData.set(key, val)
    
    elif key == "rotation":
        CamData.set(key, val)
        
    elif key == "brightness":
        CamData.set(key, val)
            
f.close()

# Camera Setup
camera = picamera.PiCamera(resolution = CamData.get("resolution"), framerate = CamData.get("framerate"))
camera.rotation = CamData.get("rotation")
camera.brightness = CamData.get("brightness")

# Basic HTML solution to stream the mjpg captured from PiCamera (not a front end guy as you can see..).
HTML="""
<html>
<head>
<title>PumuKam</title>
</head>
<body>
<center><h1> Pumuky en riguroso directo </h1></center>
<center><img src="stream.mjpg" width='1920' height='1080' autoplay playsinline></center>
</body>
</html>
"""

# Stream Setup
StreamProps = ps.StreamProps
StreamProps.set_Page(StreamProps,HTML)
address = ('192.168.1.142',8000)
StreamProps.set_Mode(StreamProps,'picamera')