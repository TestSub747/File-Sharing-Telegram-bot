from operator import add
import os
import logging


# import dotenv
# dotenv.load_dotenv()


from logging.handlers import RotatingFileHandler

#force user to join your backup channel leave 0 if you don't need.
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002280762224"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002291502234"))

if FORCE_SUB_CHANNEL > FORCE_SUB_CHANNEL2:
    temp = FORCE_SUB_CHANNEL2 
    FORCE_SUB_CHANNEL2 = FORCE_SUB_CHANNEL
    FORCE_SUB_CHANNEL = temp

#bot stats
BOT_STATS_TEXT = os.environ.get("BOTS_STATS_TEXT","<b>BOT UPTIME </b>\n{uptime}")
#send custom message when user interact with bot
USER_REPLY_TEXT = os.environ.get("USER_REPLY_TEXT", "🔒 ONLY ADMIN CAN ACCESS! 🔒\n🚀 Want to create your own private file-sharing bot?\n📩 Contact: @hf_owner\n📢 Channel: @hacking_freak</b>")

#your bot token here from https://telegram.me/BotFather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "") 
#your api id from https://my.telegram.org/apps
APP_ID = int(os.environ.get("APP_ID", "20202379"))
#your api hash from https://my.telegram.org/apps
API_HASH = os.environ.get("API_HASH", "cb1d30a2facf3a1d5691fe3dbe8e8482")
#your channel_id from https://t.me/MissRose_bot by forwarding dummy message to rose and applying command `/id` in reply to that message
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002433429310"))
#your id of telegram can be found by https://t.me/MissRose_bot with '/id' command
OWNER_ID = int(os.environ.get("OWNER_ID", "7590766084"))
#port set to default 8080
PORT = os.environ.get("PORT", "8080")
#your database url mongodb only You can use mongo atlas free cloud database
DB_URL = os.environ.get("DB_URL", "mongodb+srv://nsa837967:xJpEyfDRqgzORt4m@cluster0.m73oa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
#your database name
DB_NAME = os.environ.get("DB_NAME", "filestorebot")

#for creating telegram thread for bot to improve performance of the bot
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "60"))
#your start default command message.
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}! 👋\nI can securely store private files in a specified channel, allowing other users to access them through a special link.\n🚀 Created By: @hacking_freak")
#your telegram tag without @
OWNER_TAG = os.environ.get("OWNER_TAG", "@otpkaseller")
#Time in seconds for message delete, put 0 to never delete
TIME = int(os.environ.get("TIME", "300"))


#Shortner (token system) 
"""
some token verification sites
https://dashboard.shareus.io/
"""

# Turn this feature on or off using True or False put value inside  ""
# TRUE for yes FALSE if no 
USE_SHORTLINK = True if os.environ.get('USE_SHORTLINK', "TRUE") == "TRUE" else False 
# only shareus service known rightnow rest you can test on your own
SHORTLINK_API_URL = os.environ.get("SHORTLINK_API_URL", "modijiurl.com")
# SHORTLINK_API_KEY = os.environ.get("SHORTLINK_API_KEY", "")
#use this key if not working ☠️ (jokin!!)
SHORTLINK_API_KEY = os.environ.get("SHORTLINK_API_KEY", "e886ea0af8839407a1b27bdf760e2ab00c09d082")
#add your custom time in secs for shortlink expiration.
# 24hr = 86400
# 12hr = 43200
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', "86400")) # Add time in seconds
#put TRUE if you want shortner in every link generated by the bot.
U_S_E_P = True if (True if os.environ.get('U_S_E_P', "FALSE") == "TRUE" else False) and (USE_SHORTLINK) else False
#Tutorial video for the user of your shortner on how to download.
TUT_VID = os.environ.get("TUT_VID","https://t.me/openshort_links/12")





#Payment to remove the token system
#put TRUE if you want this feature
USE_PAYMENT = True if (True if os.environ.get("USE_PAYMENT", "TRUE") == "TRUE" else False) and (USE_SHORTLINK) else False
#UPI ID
UPI_ID = os.environ.get("UPI_ID", " TRY QR CODE FOR MOW ")
#UPI QR CODE IMAGE
UPI_IMAGE_URL = os.environ.get("UPI_IMAGE_URL", " @owner_details ")
#SCREENSHOT URL of ADMIN for verification of payments
SCREENSHOT_URL = os.environ.get("SCREENSHOT_URL", f"t.me/supplywalah_support_bot")
#Time and its price
#7 Days
PRICE1 = os.environ.get("PRICE1", "₹40 / 0.5$")
#1 Month
PRICE2 = os.environ.get("PRICE2", "₹119 / 1.5$")
#3 Month
PRICE3 = os.environ.get("PRICE3", "₹289 / 3.6$")
#6 Month
PRICE4 = os.environ.get("PRICE4", "₹549 / 6.6$")
#1 Year
PRICE5 = os.environ.get("PRICE5", "₹789 / 9.6$")



#force message for joining the channel
FORCE_MSG = os.environ.get("FORCE_MSG", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b> 🥺")
#custom caption 
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "Uploaded By @Supplywalah")
#protected content so that no files can be sent from the bot to anyone. recommended False
# TRUE for yes FALSE if no
PROTECT_CONTENT = True if os.environ.get("PROTECT_CONTENT", "TRUE") == "TRUE" else False
#used if you dont need buttons on database channel.
# True for yes False if no
DISABLE_CHANNEL_BUTTON = True if os.environ.get("DISABLE_CHANNEL_BUTTON", "FALSE") == "TRUE" else False
#you can add admin inside the bot(bug right now will fix later)

#add admins with space seperated
# 7195990000 289371935 248979023
ADMIN_LIST = os.environ.get("ADMINS", "").split()




#no need to add anything from now on
ADMINS = [int(admin) for admin in ADMIN_LIST if admin.isdigit()]
ADMINS.append(OWNER_ID)


LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)

logging.getLogger("pyrogram").setLevel(logging.WARNING)
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
