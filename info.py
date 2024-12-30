import re
from os import environ
from Script import script

def is_enabled(type, value):
    data = environ.get(type, str(value))
    if data.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif data.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        print(f'Error - {type} is invalid, exiting now')
        exit()

def is_valid_ip(ip):
    ip_pattern = r'\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
    return re.match(ip_pattern, ip) is not None

# Bot information
API_ID = environ.get('API_ID', '29265798')
if len(API_ID) == 0:
    print('Error - API_ID is missing, exiting now')
    exit()
else:
    API_ID = int(API_ID)
API_HASH = environ.get('API_HASH', '9dd673fa7291fb5a954902ea10fc8cb5')
if len(API_HASH) == 0:
    print('Error - API_HASH is missing, exiting now')
    exit()
BOT_TOKEN = environ.get('BOT_TOKEN', '')
if len(BOT_TOKEN) == 0:
    print('Error - BOT_TOKEN is missing, exiting now')
    exit()
PORT = int(environ.get('PORT', '8080'))
USER_STRING_SESSION = environ.get('USER_STRING_SESSION', '1BVtsOKEBu7SQF8Ck5YduBg9nXiMW9RHtI7x54sGunU6baup5j7Q3oPCF90PFNGjAY0Rh0X6mm1-GwMixKrb7wtgoHsX-j-ZCxYAW8OXnuAGUhbAC0Osff7I0mOxFT-Ropf579sHfd3dK87V_G9GZh84NwbloLdWCrFstAZdjeweBLlUpdpWQsvu11yWD63iN7d1VxmiV1-mo1A7LPe4zPz41fd057m9r-xpnd_M1bAEe5SAWArq_h4IPhWNkakvMxf5CrKg7V7kVK3AyqhDxe5HEE0_nxFSDXXxiBfj9G6k8LwXpnjy3MXG5d5JbWw9Yhj3REtsLRRAkImh7l7sMxOUd_-AMyR8=')

# Bot pics
PICS = (environ.get('PICS', 'https://envs.sh/8NH.jpg')).split()

# Bot Admins
ADMINS = environ.get('ADMINS', '6552970915')
if len(ADMINS) == 0:
    print('Error - ADMINS is missing, exiting now')
    exit()
else:
    ADMINS = [int(admins) for admins in ADMINS.split()]

# Channels
INDEX_CHANNELS = [int(index_channels) if index_channels.startswith("-") else index_channels for index_channels in environ.get('INDEX_CHANNELS', '-1002457424722 -1002439854017').split()]
if len(INDEX_CHANNELS) == 0:
    print('Info - INDEX_CHANNELS is empty')
LOG_CHANNEL = environ.get('LOG_CHANNEL', '-1002237007652)
if len(LOG_CHANNEL) == 0:
    print('Error - LOG_CHANNEL is missing, exiting now')
    exit()
else:
    LOG_CHANNEL = int(LOG_CHANNEL)
MOVIE_UPDATE_CHANNEL = [int(movie_update_channel) if movie_update_channel.startswith("-") else movie_update_channel for movie_update_channel in environ.get('MOVIE_UPDATE_CHANNEL', '-1002090374492').split()]
FORCE_SUB = [int(force_sub) if force_sub.startswith("-") else force_sub for force_sub in environ.get('FORCE_SUB', '-1002090374492').split()]
if len(FORCE_SUB) == 0:
    print('Info - FORCE_SUB is empty')
# For Forwarding 
SOURCE_CHANNELS1 = int(environ.get('SOURCE_CHANNELS1', '-1002439854017')) # 1TamilBlasters
SOURCE_CHANNELS2 = int(environ.get('SOURCE_CHANNELS2', '-1001864825324')) # 1TamilMV
SOURCE_CHANNELS3 = int(environ.get('SOURCE_CHANNELS3', '-1001822541447')) # 1TamilBlasters
SOURCE_CHANNELS4 = int(environ.get('SOURCE_CHANNELS4', '-1001864825324')) # 1TamilMV
SOURCE_CHANNELS5 = int(environ.get('SOURCE_CHANNELS5', '-1001822541447')) # 1TamilBlasters
SOURCE_CHANNELS6 = int(environ.get('SOURCE_CHANNELS6', '-1001864825324')) # 1TamilMV
SOURCE_CHANNELS7 = int(environ.get('SOURCE_CHANNELS7', '2082930520'))

# support group
SUPPORT_GROUP = environ.get('SUPPORT_GROUP', '-1002256368276')
if len(SUPPORT_GROUP) == 0:
    print('Error - SUPPORT_GROUP is missing, exiting now')
    exit()
else:
    SUPPORT_GROUP = int(SUPPORT_GROUP)

# MongoDB information
DATABASE_URL = environ.get('DATABASE_URL', "mongodb+srv://KarthikMovies:KarthikUK007@cluster0.4l5byki.mongodb.net/?retryWrites=true&w=majority")
if len(DATABASE_URL) == 0:
    print('Error - DATABASE_URL is missing, exiting now')
    exit()
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Files')

# Links
SUPPORT_LINK = environ.get('SUPPORT_LINK', 'https://t.me/UpperZoneBot')
OWNER_USERNAME = environ.get("OWNER_USERNAME", "https://t.me/Kanus_Network")
UPDATES_LINK = environ.get('UPDATES_LINK', 'https://t.me/Movies_4_Download')
FILMS_LINK = environ.get('FILMS_LINK', 'https://t.me/Movies_4_Download')
TUTORIAL = environ.get("TUTORIAL", "https://t.me/Movies_4_Download/22")
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/Movies_4_Download/22")

# Bot settings
DELETE_TIME = int(environ.get('DELETE_TIME', 3600)) # Add time in seconds
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
MAX_BTN = int(environ.get('MAX_BTN', 10))
LANGUAGES = [language.lower() for language in environ.get('LANGUAGES', 'tamil hindi english telugu kannada malayalam marathi punjabi').split()]
QUALITY = [quality.lower() for quality in environ.get('QUALITY', '360p 480p 720p 1080p 2160p').split()]
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", script.IMDB_TEMPLATE)
FILE_CAPTION = environ.get("FILE_CAPTION", script.FILE_CAPTION)
SHORTLINK_URL = environ.get("SHORTLINK_URL", "publicearn.com")
SHORTLINK_API = environ.get("SHORTLINK_API", "6b30ad861a51b05f8dc26311c5b72b5038f2cdee")
VERIFY_EXPIRE = int(environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds (1 Day)
WELCOME_TEXT = environ.get("WELCOME_TEXT", script.WELCOME_TEXT)
INDEX_EXTENSIONS = [extensions.lower() for extensions in environ.get('INDEX_EXTENSIONS', 'mp4 mkv').split()]
PM_FILE_DELETE_TIME = int(environ.get('PM_FILE_DELETE_TIME', '3600'))

# boolean settings
IS_PM_SEARCH = is_enabled('IS_PM_SEARCH', True)
IS_VERIFY = is_enabled('IS_VERIFY', False)
IS_SEND_MOVIE_UPDATE = is_enabled('IS_SEND_MOVIE_UPDATE', True) # Don't Change It ( If You Want To Turn It On Then Turn It On By Commands) We Suggest You To Make It Turn Off If You Are Indexing Files First Time.
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
WELCOME = is_enabled('WELCOME', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
LONG_IMDB_DESCRIPTION = is_enabled("LONG_IMDB_DESCRIPTION", False)
LINK_MODE = is_enabled("LINK_MODE", True)
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
IMDB = is_enabled('IMDB', True)
SPELL_CHECK = is_enabled("SPELL_CHECK", True)
SHORTLINK = is_enabled('SHORTLINK', False)

#premium info
PAYMENT_QR = environ.get('PAYMENT_QR', 'https://envs.sh/8NH.jpg')
OWNER_UPI_ID = environ.get('OWNER_UPI_ID', 'Contact At @rj_09_kanhaiya')

# RSS Feed URL
TAMILMV = environ.get("TMV", "https://www.1tamilmv.uno/")
TAMILBLAST = environ.get("TB", "https://www.1tamilblasters.party/")
TAMILROCKERS = environ.get("TR", "https://www.2tamilrockers.com/")
# log channel list
TAMILMV_LOG = int(environ.get("TMV_LOG", -1002237007652))
TAMILBLAST_LOG = int(environ.get("TB_LOG", -1002237007652))
TAMILROCKERS_LOG = int(environ.get("TR_LOG", -1002237007652))

# for stream
IS_STREAM = is_enabled('IS_STREAM', True)
BIN_CHANNEL = environ.get("BIN_CHANNEL", "-1002410949273")
if len(BIN_CHANNEL) == 0:
    print('Error - BIN_CHANNEL is missing, exiting now')
    exit()
else:
    BIN_CHANNEL = int(BIN_CHANNEL)
URL = environ.get("URL", "https://dpbotz-player.koyeb.app/")
if len(URL) == 0:
    print('Error - URL is missing, exiting now')
    exit()
else:
    if URL.startswith(('https://', 'http://')):
        if not URL.endswith("/"):
            URL += '/'
    elif is_valid_ip(URL):
        URL = f'http://{URL}/'
    else:
        print('Error - URL is not valid, exiting now')
        exit()
