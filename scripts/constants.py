import os
from dotenv import load_dotenv

load_dotenv()

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_USERNAME = os.environ.get("TWITTER_USERNAME")
TWITTER_EMAIL = os.environ.get("TWITTER_EMAIL")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")
EXTENSION_PATH = "scripts/OMGHFJLPGGMJJAAGOCLMMOBGDODCJBOH_3_85_7_0.crx"