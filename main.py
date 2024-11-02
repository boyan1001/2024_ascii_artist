from PIL import Image

# ASCII_CHARS = " %@#*+=-:.  "
ASCII_CHARS = "@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%############################*****************************++++++++++++++++++++++++++++============================-----------------------------::::::::::::::::::::::::::::............................               "

def resize_gray_image(image, new_width=256):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.5)
    resized_image = image.resize((new_width, new_height))
    gray_image = resized_image.convert("L")
    return gray_image

def image_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel * (len(ASCII_CHARS) - 1) // 255] for pixel in pixels])
    ascii_image = [ascii_str[index: index + image.width] for index in range(0, len(ascii_str), image.width)]
    return "\n".join(ascii_image)



image_path = './assert/e57a8340-d13e-4886-aa61-6fe8c06c5432.jpg'

file = open('output3.txt', 'w', encoding='utf-8')

try:
    image = Image.open(image_path)
except Exception as e:
    file.write(f"Error opening image: {e}")
else:
    gray_image = resize_gray_image(image)
    ascii_art = image_to_ascii(gray_image)
    file.write(ascii_art)

file.close()