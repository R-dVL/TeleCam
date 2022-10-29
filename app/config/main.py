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