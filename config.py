from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "22535895"))
API_HASH = getenv("API_HASH", "368abe51e77d16b3774661b4ce59b26e")
BOT_TOKEN = getenv("BOT_TOKEN", "5497887119:AAGLz5H5aprth55WfYZdsfkR0KBNSIk4z8w")
SESSION_NAME = getenv("SESSION_NAME", "BACx4IQcv5lr41bK01o2HPN2YsL99k36pUzOmZvNxNPrGARuqKq5H0JCCfx4k4ciMtcBnk3lUVnl-MjZFu5sIaoD2oYy8Qr5nCaQN4GPDBcdIY8g8Bqh_89w6yZrII7CedJ1uTTV2v038PvN1joSb5KkOZCDS8n5REpUDHmZ88VZKMR65p3b5OmiaOgQlnzkkclSchjiUAIaWPbWXlA-R6RDb7QcUKaiq5dZMs8asSSipv9sWpezDZKyaDKYPgxrefyMr6qopT6FKLfAhho5tx6YwQE2l1_DF-2gEOhARF0V6s-l0GsbDLzKSxFS-VyyIU2h0rbrHi79Ac8MHxGBGVnDAAAAAWBEaEkA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "c_l_h")
ALIVE_NAME = getenv("ALIVE_NAME", "sonng")
BOT_USERNAME = getenv("BOT_USERNAME", "Gotcar_bot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/X02lx/RrRRR")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "goto90")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "goto90")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "5355696037").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "c_l_h").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
