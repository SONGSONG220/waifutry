class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7078181502"
    sudo_users = "7378476666", "7180469677", "7078181502"
    GROUP_ID = -1002009280180
    TOKEN = "7698227314:AAGm91L70r1mYcnYc5oGcz_R4AHuNl899aw"
    mongo_url = "mongodb+srv://I-LOVE-PDF-BOT:I-LOVE-PDF-BOT@cluster0.c51o3a9.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/dc0aa314d28a67af0ee83.jpg", "https://telegra.ph/file/e3bdc6e1f14191e058ea7.jpg", "https://telegra.ph/file/dc0aa314d28a67af0ee83.jpg"]
    SUPPORT_CHAT = "-1002289810575"
    UPDATE_CHAT = "PiratesBotRepo"
    BOT_USERNAME = "husbanduCollector_Bot"
    CHARA_CHANNEL_ID = "-1002412957777"
    api_id = 22792918
    api_hash = "ff10095d2bb96d43d6eb7a7d9fc85f81"
    
    STRICT_GBAN = True
    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
