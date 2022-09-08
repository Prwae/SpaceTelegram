import requests
from pprint import pprint
from download_image import download_image
import argparse
import os


def fetch_spacex_last_launch(directory, launch_id):
    payload = {
        "id": launch_id
    }

    if launch_id == "latest":
        response = requests.get("https://api.spacexdata.com/v5/launches/latest")
    else:
        response = requests.get(f"https://api.spacexdata.com/v5/launches/:id", params=payload)
    response.raise_for_status()
    pprint(response.json())
    print(type(response.json()))
    for num, image in enumerate(response.json()[0]["links"]["flickr"]["original"]):
        download_image(image, os.path.join(directory, f"spacex{num}"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--launch_id', help='ID запуска', type=str, default="5eb87d42ffd86e000604b384")
    launch_id = parser.parse_args().launch_id

    os.makedirs("images", exist_ok=True)

    if launch_id:
        fetch_spacex_last_launch("images", launch_id)
    else:
        fetch_spacex_last_launch("images")
