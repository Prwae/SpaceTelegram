import requests
from download_image import download_image
import os
from dotenv import load_dotenv
from urllib.parse import urlparse


def get_file_extension(link):
    return os.path.splitext(urlparse(link).path)[1]


def fetch_apod(apikey, directory):
    count = 30
    payload = {
        "api_key": apikey,
        "count": count
    }

    response = requests.get(f"https://api.nasa.gov/planetary/apod", params=payload)
    response.raise_for_status()

    for img_number, apod in enumerate(response.json()):
        download_image(apod["url"], os.path.join(directory, f"apod{img_number}{get_file_extension(apod['url'])}"))


if __name__ == "__main__":
    os.makedirs("images", exist_ok=True)

    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]

    fetch_apod(nasa_token, "images")
