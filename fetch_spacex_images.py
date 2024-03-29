import requests
from general_functions import download_image, get_file_extension
import argparse
import os


def fetch_spacex_last_launch(directory, launch_id):
    response = requests.get(f"https://api.spacexdata.com/v5/launches/{launch_id}")
    response.raise_for_status()

    for num, image in enumerate(response.json()["links"]["flickr"]["original"]):
        download_image(image, os.path.join(directory, f"spacex{num}{get_file_extension(image)}"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--launch_id', help='ID запуска', type=str, default="latest")
    launch_id = parser.parse_args().launch_id

    os.makedirs("images", exist_ok=True)

    fetch_spacex_last_launch("images", launch_id)

