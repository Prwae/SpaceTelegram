from urllib.parse import urlsplit
import os
import time
from random import *

import requests
import telegram
from dotenv import load_dotenv


def image_download(url, way):
    response = requests.get(url)
    response.raise_for_status()

    with open(way, "wb") as file:
        file.write(response.content)


def get_file_extension(link):
    return os.path.splitext(urlsplit(link)[2])[1]


def fetch_spacex_last_launch():
    response = requests.get("https://api.spacexdata.com/v4/launches/latest")
    response.raise_for_status()

    json_response = response.json()

    for id, image in enumerate(json_response["links"]["flickr"]["original"]):
        image_download(image, f"images/spacex{id}.jpeg")


def get_apod(count, apikey):
    response = requests.get(
        f"https://api.nasa.gov/planetary/apod?api_key={apikey}&count={count}")
    response.raise_for_status()

    json_response = response.json()

    for id, apod in enumerate(json_response):
        print(apod["url"])
        image_download(apod["url"], f"images/apod{id}{get_file_extension(apod['url'])}")


def get_epic(apikey):
    response = requests.get(f"https://api.nasa.gov/EPIC/api/natural?api_key={apikey}")
    response.raise_for_status()

    json_response = response.json()

    for id, epic in enumerate(json_response):
        url = f"https://api.nasa.gov/EPIC/archive/natural/{epic['date'][0:10].replace('-', '/')}/png/{epic['image']}.png?api_key=EJBgaOeDsQVkfNFTgcPDX3kyrddUCkl56CH4qOqh"
        image_download(url, f"images/epic{id}.jpeg")


def telegram_post():
    while True:
        image_choice = choice(os.listdir("images"))
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
    telegram_post()
