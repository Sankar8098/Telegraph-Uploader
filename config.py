import os

class Config:

    API_ID = int(os.environ.get("API_ID", 23990433))
    API_HASH = os.environ.get("API_HASH","e6c4b6ee1933711bc4da9d7d17e1eb20")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5908996043:AAEgqJBgtuju5K0jijTSmAk6enEZMk4j2dA")
