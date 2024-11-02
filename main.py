from PIL import Image

ASCII_CHARS = "@%#*+=-:. "

def resize_gray_image(image, new_width=1000):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.5)
    resized_image = image.resize((new_width, new_height))
    gray_image = resized_image.convert("L")
    return gray_image

def image_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    ascii_image = [ascii_str[index: index + image.width] for index in range(0, len(ascii_str), image.width)]
    return "\n".join(ascii_image)



image_path = './assert/test3.png'

try:
    image = Image.open(image_path)
except Exception as e:
    print(f"Error opening image: {e}")
else:
    gray_image = resize_gray_image(image)
    ascii_art = image_to_ascii(gray_image)
    print(ascii_art)
