import os
import time
import random
import requests
import telegram
from dotenv import load_dotenv
import argparse


def post_images_to_telegram(directory, chat_id, image_send_peridiocity):
    while True:
        image_choice = random.choice(os.listdir("images"))
        with open(os.path.join(directory, image_choice), "rb") as file:
            bot.send_photo(chat_id=chat_id, photo=file)
        time.sleep(image_send_peridiocity)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('image_send_periodicity', help='Периодичность отправки фото', type=int)
    image_send_periodicity = parser.parse_args().image_send_periodicity

    os.makedirs("images", exist_ok=True)
    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]
    telegram_token = os.environ["TELEGRAM_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHANNEL"]
    bot = telegram.Bot(token=telegram_token)

    post_images_to_telegram("images", chat_id, image_send_periodicity)
