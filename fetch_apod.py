import requests
from general_functions import download_image, get_file_extension
import os
from dotenv import load_dotenv
import argparse


def fetch_apod(apikey, directory, count):
    payload = {
        "api_key": apikey,
        "count": count
    }

    response = requests.get(f"https://api.nasa.gov/planetary/apod", params=payload)
    response.raise_for_status()
    for num, apod in enumerate(response.json()):
        if apod["media_type"] == "image":
            download_image(apod["url"], os.path.join(directory, f"apod{num}{get_file_extension(apod['url'])}"), params=payload)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_count', help='Количество фотографий', type=int, default=30)
    image_count = parser.parse_args().image_count

    os.makedirs("images", exist_ok=True)

    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]

    fetch_apod(nasa_token, "images", image_count)

