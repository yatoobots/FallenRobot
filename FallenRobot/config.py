class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 25898978
    API_HASH = "8b0f2179ed27f83222d344bb6959d00c"

    CASH_API_KEY = "YatooXD"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://lvrxsynk:OMujzREX_Ha1jO2qh20qTmDMAoMRwBbh@trumpet.db.elephantsql.com/lvrxsynk"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1001889157016)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://Yatoo99:Yatoo99@cluster0.3gj7zms.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/40eb1ed850cdea274693e.jpg"

    SUPPORT_CHAT = "sympathee"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6264504776:AAEy_sOU9fckQyH6GD7ZBN1NPhlVAJRDgvo"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "YatooXD"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 5264219629  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
