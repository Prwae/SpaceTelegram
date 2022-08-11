import requests
from pprint import pprint
from download_image import download_image
import argparse
import os


def fetch_spacex_last_launch(directory, launch_number="latest"):
    if launch_number == "latest":
        response = requests.get("https://api.spacexdata.com/v4/launches/latest")
    else:
        response = requests.get(f"https://api.spacexdata.com/v3/launches/{launch_number}")
    response.raise_for_status()
    for img_number, image in enumerate(response.json()["links"]["flickr_images"]):
        download_image(image, f"{directory}spacex{img_number}.jpeg")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--launch_number', help='Номер запуска', type=int)
    launch_number = parser.parse_args().launch_number

    os.makedirs("images", exist_ok=True)

    if launch_number:
        fetch_spacex_last_launch("images/", launch_number)
    else:
        fetch_spacex_last_launch("images/")
