# These methods are created in order to protect the token and chat ID of the bot
class botdata:
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
        return bot.__conf[name]
    
    # Setter method
    @staticmethod
    def set(name, value):
        if name in botdata.__setters:
            botdata.__config[name] = value
        else:
            raise NameError("Not accepted configuration.")