import requests
import os
from urllib.parse import urlparse


def get_file_extension(link):
    return os.path.splitext(urlparse(link).path)[1]


def download_image(url, path, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()

    with open(path, "wb") as file:
        file.write(response.content)
