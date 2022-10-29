# These methods are created in order to protect the token and chat ID of the bot
class Data:
    __config = {
        "token": "",
        "chat": "",
        "video": "",
        "photo": ""
    }
    __setters = ["token", "chat", "video", "photo"]
    
    # Getter method
    @staticmethod
    def get(name):
        return Data.__config[name]
    
    # Setter method
    @staticmethod
    def set(name, value):
        if name in Data.__setters:
            Data.__config[name] = value
        else:
            raise NameError("Not accepted configuration.")
        
def bot_setup():
    Data.set("token", "5572530259:AAEXUMX0R6HmoBIy3akphPOv7bLZjPEX-Bw")
    Data.set("chat", "-1001743800156")
    Data.set("video", "/home/rdvl/Documents/GitHub/Python-TeleCam/data/video")
    Data.set("photo", "/home/rdvl/Documents/GitHub/Python-TeleCam/data/photo")
    
if __name__ == "__main__":
    BotData = Data
    bot_setup()
    print(BotData.get("token"))