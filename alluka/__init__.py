import logging
import os
import sys
import time
import telegram.ext as tg

StartTime = time.time()

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO)

LOGGER = logging.getLogger(__name__)

# if version < 3.6, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error("You MUST have a python version of at least 3.6! Multiple features depend on this. Bot quitting.")
    quit(1)

ENV = bool(os.environ.get('ENV', False))

if ENV:
    TOKEN = os.environ.get('TOKEN', None)

    try:
        OWNER_ID = int(os.environ.get('OWNER_ID', None))
    except ValueError:
        raise Exception("Your OWNER_ID env variable is not a valid integer.")

    MESSAGE_DUMP = os.environ.get('MESSAGE_DUMP', None)
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", None)

    try:
        SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
        DEV_USERS = set(int(x) for x in os.environ.get("DEV_USERS", "").split())
    except ValueError:
        raise Exception("Your sudo or dev users list does not contain valid integers.")

    try:
        SUPPORT_USERS = set(int(x) for x in os.environ.get("SUPPORT_USERS", "").split())
    except ValueError:
        raise Exception("Your support users list does not contain valid integers.")

    try:
        SPAMMERS = set(int(x) for x in os.environ.get("SPAMMERS", "").split())
    except ValueError:
        raise Exception("Your spammers users list does not contain valid integers.")

    try:
        WHITELIST_USERS = set(int(x) for x in os.environ.get("WHITELIST_USERS", "").split())
    except ValueError:
        raise Exception("Your whitelisted users list does not contain valid integers.")

    #ZOLDYCK_FAIMLY_LIST
    ALLUKA = os.environ.get('ALLUKA', None)
    HISOKA = os.environ.get('HISOKA', None)
    GING = os.environ.get('GING', None)
    SHIZUKU = os.environ.get('SHIZUKU', None)
    SILVA = os.environ.get('SILVA', None)
    GON = os.environ.get('GON', None)
    ILLUMI_ZOLDYCK = os.environ.get('ILLUMI_ZOLDYCK', None)
    LEORIO = os.environ.get('LEORIO', None)
    BISCUIT = os.environ.get('BISCUIT', None)
    CHROLLO = os.environ.get('CHROLLO', None)
    KILLUA = os.environ.get('KILLUA', None)
    MERUEM = os.environ.get('MERUEM', None)
    KITE = os.environ.get('KITE', None)
    
    


    GBAN_LOGS = os.environ.get('GBAN_LOGS', None)
    WEBHOOK = bool(os.environ.get('WEBHOOK', False))
    URL = os.environ.get('URL', "")  # Does not contain token
    PORT = int(os.environ.get('PORT', 5000))
    CERT_PATH = os.environ.get("CERT_PATH")

    DB_URI = os.environ.get('DB_URI')
    DONATION_LINK = os.environ.get('DONATION_LINK')
    LOAD = os.environ.get("LOAD", "").split()
    NO_LOAD = os.environ.get("NO_LOAD", "translation").split()
    DEL_CMDS = bool(os.environ.get('DEL_CMDS', False))
    STRICT_GBAN = bool(os.environ.get('STRICT_GBAN', False))
    WORKERS = int(os.environ.get('WORKERS', 8))
    BAN_STICKER = os.environ.get('BAN_STICKER', 'CAACAgUAAxkBAAIHsl5nbqXdDTmpG2HFDNhnwvE5kFbWAAI9AQAC3pTNLzeTCUmnhTneGAQ')
    ALLOW_EXCL = os.environ.get('ALLOW_EXCL', False)
    CASH_API_KEY = os.environ.get('CASH_API_KEY', None)
    TIME_API_KEY = os.environ.get('TIME_API_KEY', None)
    WALL_API = os.environ.get('WALL_API',None)
    LASTFM_API_KEY = os.environ.get('LASTFM_API_KEY',None)

else:
    from alluka.config import Development as Config
    TOKEN = Config.API_KEY

    try:
        OWNER_ID = int(Config.OWNER_ID)
    except ValueError:
        raise Exception("Your OWNER_ID variable is not a valid integer.")

    MESSAGE_DUMP = Config.MESSAGE_DUMP
    OWNER_USERNAME = Config.OWNER_USERNAME

    try:
        SUDO_USERS = set(int(x) for x in Config.SUDO_USERS or [])
        DEV_USERS = set(int(x) for x in Config.DEV_USERS or [])
    except ValueError:
        raise Exception("Your sudo or dev users list does not contain valid integers.")

    try:
        SUPPORT_USERS = set(int(x) for x in Config.SUPPORT_USERS or [])
    except ValueError:
        raise Exception("Your support users list does not contain valid integers.")

    try:
        SPAMMERS = set(int(x) for x in Config.SPAMMERS or [])
    except ValueError:
        raise Exception("Your spammers users list does not contain valid integers.")

    try:
        WHITELIST_USERS = set(int(x) for x in Config.WHITELIST_USERS or [])
    except ValueError:
        raise Exception("Your whitelisted users list does not contain valid integers.")

    GBAN_LOGS = Config.GBAN_LOGS
    WEBHOOK = Config.WEBHOOK
    URL = Config.URL
    PORT = Config.PORT
    CERT_PATH = Config.CERT_PATH

    DB_URI = Config.DB_URI
    DONATION_LINK = Config.DONATION_LINK
    LOAD = Config.LOAD
    NO_LOAD = Config.NO_LOAD
    DEL_CMDS = Config.DEL_CMDS
    STRICT_GBAN = Config.STRICT_GBAN
    WORKERS = Config.WORKERS
    BAN_STICKER = Config.BAN_STICKER
    ALLOW_EXCL = Config.ALLOW_EXCL
    CASH_API_KEY = Config.CASH_API_KEY
    TIME_API_KEY = Config.TIME_API_KEY
    WALL_API = Config.WALL_API
    LASTFM_API_KEY = Config.LASTFM_API_KEY

    #ZOLDYCK_FAMMILY
    ALLUKA = Config.ALLUKA
    HISOKA = Config.HISOKA
    GING = Config.GING
    SHIZUKU = Config.SHIZUKU
    SILVA = Config.SILVA
    GON = Config.GON
    ILLUMI_ZOLDYCK = Config.ILLUMI_ZOLDYCK 
    LEORIO = Config.LEORIO
    BISCUIT = Config.BISCUIT
    CHROLLO = Config.CHROLLO
    KILLUA =  Config.KILLUA
    MERUEM =  Config.MERUEM
    KITE =  Config.KITE
    
    
    

SUDO_USERS.add(OWNER_ID)
DEV_USERS.add(OWNER_ID)

updater = tg.Updater(TOKEN, workers=WORKERS)
dispatcher = updater.dispatcher

SUDO_USERS = list(SUDO_USERS) + list(DEV_USERS)
DEV_USERS = list(DEV_USERS)
WHITELIST_USERS = list(WHITELIST_USERS)
SUPPORT_USERS = list(SUPPORT_USERS)
SPAMMERS = list(SPAMMERS)

# Load at end to ensure all prev variables have been set
from alluka.modules.helper_funcs.handlers import CustomCommandHandler, CustomRegexHandler, CustomMessageHandler

# make sure the regex handler can take extra kwargs
tg.RegexHandler = CustomRegexHandler
tg.CommandHandler = CustomCommandHandler
tg.MessageHandler = CustomMessageHandler

def spamfilters(text, user_id, chat_id):
    #print("{} | {} | {}".format(text, user_id, chat_id))
    if int(user_id) in SPAMMERS:
        print("This user is a spammer!")
        return True
    else:
        return False
