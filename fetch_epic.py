import requests
from datetime import datetime
from download_image import download_image
import os
from dotenv import load_dotenv


def fetch_epic(apikey, directory):
    payload = {
        "api_key": apikey
    }

    response = requests.get(f"https://api.nasa.gov/EPIC/api/natural", params=payload)
    response.raise_for_status()

    for img_id, epic in enumerate(response.json()):
        datetime_date = datetime.strptime(epic["date"], "%Y-%m-%d %H:%M:%S")
        formatted_date = datetime_date.strftime("%Y/%m/%d")
        url = f"https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{epic['image']}.png"
        download_image(url, os.path.join(directory, f"epic{img_id}"))


if __name__ == "__main__":
    os.makedirs("images", exist_ok=True)

    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]

    fetch_epic(nasa_token, "images")
