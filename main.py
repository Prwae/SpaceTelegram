import logging
import os
import time
import random
import telegram
from dotenv import load_dotenv
import argparse


def post_images_to_telegram(directory, chat_id, sec_delay):
    while True:
        image_path = random.choice(os.listdir("images"))
        try:
            with open(os.path.join(directory, image_path), "rb") as file:
                bot.send_photo(chat_id=chat_id, photo=file)
            time.sleep(sec_delay)
        except telegram.error.NetworkError:
            logging.warning("Не удалось подключиться к серверу. Проверьте подключение к интернету.")
            time.sleep(5)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_send_periodicity', help='Периодичность отправки фото', type=int, default=14400)
    sec_delay = parser.parse_args().sec_delay

    os.makedirs("images", exist_ok=True)
    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]
    telegram_token = os.environ["TELEGRAM_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHANNEL"]
    bot = telegram.Bot(token=telegram_token)

    post_images_to_telegram("images", chat_id, sec_delay)
