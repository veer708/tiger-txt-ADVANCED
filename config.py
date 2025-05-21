import os

API_ID = API_ID = 29232353

API_HASH = os.environ.get("API_HASH", "6868788228291767c90e4346eea03f36")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6650855788))

LOG = -1002689649403

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6650855788").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


