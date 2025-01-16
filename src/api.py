import requests
import os
from io import BytesIO
from PIL import Image, ImageEnhance, ImageDraw, ImageFont, ImageTk

#  anime picture
def download_waifu_image(image_path):

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
            print("Failed to download image, status code:", image_response.status_code)
            return None

    else:
        print("API request failed, status code:", response.status_code)
        return None

# dog picture
def download_dog_image(image_path):
    response = requests.get('https://dog.ceo/api/breeds/image/random')

    if response.status_code == 200:
        data = response.json()
        image_url = data.get('message')

        # 下载图片
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            # 保存图片
            with open(image_path, 'wb') as file:
                file.write(image_response.content)
            print(f"Image successfully saved to: {image_path}")
        else:
            print("Failed to download image, status code:", image_response.status_code)
    else:
        print("API request failed, status code:", response.status_code)
    return image_path