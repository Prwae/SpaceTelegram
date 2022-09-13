import requests
from general_functions import download_image, get_file_extension
import os
from dotenv import load_dotenv


def fetch_apod(apikey, directory):
    count = 30
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
    os.makedirs("images", exist_ok=True)

    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]

    fetch_apod(nasa_token, "images")
