from urllib.parse import urlparse
import os
import time
import random
import requests
import telegram
from dotenv import load_dotenv
import argparse
from pprint import pprint
import datetime


def download_image(url, path, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()

    with open(path, "wb") as file:
        file.write(response.content)


def get_file_extension(link):
    return os.path.splitext(urlparse(link).path)[1]


def fetch_spacex_last_launch(directory):
    response = requests.get("https://api.spacexdata.com/v3/launches/64")
    response.raise_for_status()
    pprint(response.json())
    for img_number, image in enumerate(response.json()["links"]["flickr_images"]):
        download_image(image, f"{directory}spacex{img_number}.jpeg")


def get_apod(count, apikey, directory):
    payload = {
        "api_key": apikey,
        "count": count
    }

    response = requests.get(f"https://api.nasa.gov/planetary/apod", params=payload)
    response.raise_for_status()

    for img_number, apod in enumerate(response.json()):
        download_image(apod["url"], f"{directory}apod{img_number}{get_file_extension(apod['url'])}")


def get_epic(apikey, directory):
    payload = {
        "api_key": apikey
    }

    response = requests.get(f"https://api.nasa.gov/EPIC/api/natural", params=payload)
    response.raise_for_status()

    for img_id, epic in enumerate(response.json()):
        datetime_date = datetime.date.fromisoformat(epic["date"])
        formatted_date = datetime_date.strftime("%Y/%m/%d")
        url = f"https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{epic['image']}.png"
        download_image(url, f"{directory}epic{img_id}.jpeg", payload)


def post_images_to_telegram(directory, chat_id, image_send_peridiocity):
    while True:
        image_choice = random.choice(os.listdir("images"))
        with open(f"{directory}{image_choice}", "rb") as file:
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

    post_images_to_telegram("images/", chat_id, image_send_periodicity)
