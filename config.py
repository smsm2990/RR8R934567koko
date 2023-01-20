from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "14536751"))
API_HASH = getenv("API_HASH", "f98e40bf5c651b292e5ddf240306d0e2")
BOT_TOKEN = getenv("BOT_TOKEN","5732084506:AAGl6McC6Pf_DAPHmH8DoZs5WMV_lJcprAY")
SESSION_NAME = getenv("SESSION_NAME", "AgAtZXCktvRiDLRhIJYMgtlX7bjXmgDmvqGsJ5pn0pYW00BDRYIRepFb18-v_thXI2e55dRrWSca_lw4CzmFhmBNaULvzqCLNZqzs6WedWvb4GCvTtBGHYZc6phphVXOAFqGih1vT-VVD3ALPrTs1U-kfgb-wWC9SzcvDflyJkV4D_zMbZVgNkrkrM7EiWlCxnrp8vz7TxiJBWjRglv6No3fM7rcjB2wsTVPXJQisWmBoxbzS50l4RNRT4ErsnDzdQoWd22rkXVMKwCSzM2OJWg-873uVaj8agZA8uXBS_JSE7F8IgzvvV0_w5xsaCYuDkwsefQzhoLdBvroAZB_potcAAAAAVWT1z8A")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME","smsmkurdi")
ALIVE_NAME = getenv("ALIVE_NAME", "BEZARM1")
BOT_USERNAME = getenv("BOT_USERNAME", "M2_SPORT_BOT")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/levina-lab/video-stream")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Baravrekarast")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Baravrekarast")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "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")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID","5730719551").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS","smsmkurdi").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
