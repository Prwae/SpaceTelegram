import time
import os
from random import *

import telegram
from dotenv import load_dotenv


load_dotenv()

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = "@spacimg_p"
BOT = telegram.Bot(token='2026879259:AAEc0NRP7xOyeV_VYcoDsbqn83rU-nwsvbw')
IMAGE_CHOICE = choice(os.listdir("images"))


if __name__ == "__main__":
    while True:
        time.sleep(86400)
        BOT.send_document(chat_id=CHAT_ID, document=open(IMAGE_CHOICE, 'rb'))
