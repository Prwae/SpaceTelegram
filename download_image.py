import requests


def download_image(url, path, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()

    with open(path, "wb") as file:
        file.write(response.content)
