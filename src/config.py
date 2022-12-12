import os
from dotenv import load_dotenv

load_dotenv()

MONGO_USER = os.environ.get('MONGO_USER')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD')
MONGO_PORT = os.environ.get('MONGO_PORT')

MAIL_SENDER = os.environ.get('MAIL_SENDER')
MAIL_RECIEVER = os.environ.get('MAIL_RECIEVER')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

TOKEN = os.environ.get('TG_BOT_TOKEN')
CHAT_ID = os.environ.get('TG_CHAT_ID')

TELEGRAM_BROKER_URL = os.environ.get('TELEGRAM_BROKER_URL')
MAIL_BROKER_URL = os.environ.get('MAIL_BROKER_URL')