class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7526369190"
    sudo_users = "5268691896", "7526369190", "5884969921"
    GROUP_ID = -1002468653401
    TOKEN = "7698227314:AAGm91L70r1mYcnYc5oGcz_R4AHuNl899aw"
    mongo_url = "mongodb+srv://I-LOVE-PDF-BOT:I-LOVE-PDF-BOT@cluster0.c51o3a9.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://files.catbox.moe/hsyqp7.jpg", "https://files.catbox.moe/hsyqp7.jpg", "https://files.catbox.moe/hsyqp7.jpg"]
    SUPPORT_CHAT = "-1002466009612"
    UPDATE_CHAT = "niyoto_supoort"
    BOT_USERNAME = "husbanduCollector_Bot"
    CHARA_CHANNEL_ID = "-1002183028236"
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
