import requests
from PIL import Image
from io import BytesIO
import os

def download_waifu_image(filename="waifu_image.png"):
    """
    Download a random anime image from waifu.pics API and save it to the current directory.
    :param filename: The filename to save the image as, default is "waifu_image.png"
    :return: The path to the saved image if successful, None otherwise
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, filename)

    api_url = "https://api.waifu.pics/sfw/waifu"
    response = requests.get(api_url)

    if response.status_code == 200:
        image_url = response.json().get("url")
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            image = Image.open(BytesIO(image_response.content))
            image.save(image_path)
            print(f"Image successfully saved to: {image_path}")
            return image_path
        else:
            print("Failed to download image")
            return None
    else:
        print("API request failed")
        return None
download_waifu_image("random_waifu.png")
