from urllib.parse import urlsplit
import os
import time
import random

import requests
import telegram
from dotenv import load_dotenv


def download_image(url, way):
    response = requests.get(url)
    response.raise_for_status()

    with open(way, "wb") as file:
        file.write(response.content)


def get_file_extension(link):
    return os.path.splitext(urlsplit(link)[2])[1]


def fetch_spacex_last_launch():
    response = requests.get("https://api.spacexdata.com/v4/launches/latest")
    response.raise_for_status()

    for id, image in enumerate(response.json()["links"]["flickr"]["original"]):
        download_image(image, f"images/spacex{id}.jpeg")


def get_apod(count, apikey):
    payload = {
        apikey: apikey,
        count: count
    }

    response = requests.get(
        f"https://api.nasa.gov/planetary/apod", params=payload)
    response.raise_for_status()

    for id, apod in enumerate(response.json()):
        download_image(apod["url"], f"images/apod{id}{get_file_extension(apod['url'])}")


def get_epic(apikey):
    payload = {
        apikey: apikey
    }

    response = requests.get(f"https://api.nasa.gov/EPIC/api/natural", params=payload)
    response.raise_for_status()

    for id, epic in enumerate(response.json()):
        url = f"https://api.nasa.gov/EPIC/archive/natural/{epic['date'][0:10].replace('-', '/')}/png/{epic['image']}.png?api_key={apikey}"
        download_image(url, f"images/epic{id}.jpeg")


def post_images_to_telegram():
    while True:
        image_choice = random.choice(os.listdir("images"))
        with open(f"images/{image_choice}", "rb") as file:
            image = file.read()
        bot.send_photo(chat_id=chat_id, photo=image)
        time.sleep(86400)


if __name__ == "__main__":
    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]
    telegram_token = os.environ["TELEGRAM_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHANNEL"]
    bot = telegram.Bot(token=telegram_token)

    fetch_spacex_last_launch()
    get_apod(30, nasa_token)
    get_epic(nasa_token)
    post_images_to_telegram()
