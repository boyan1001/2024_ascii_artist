import requests
from PIL import Image, ImageEnhance, ImageDraw, ImageFont, ImageTk
from io import BytesIO
import os
import tkinter as tk

# ASCII 字符集，用於生成 ASCII 藝術
ASCII_CHARS = " .',:;\"^`i!lI><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQO0Zmwpqdbkhao*#MW&8%B@$"

# 將 RGB 值轉換為灰度值
def rgb_to_grayscale(r, g, b):
    gray = int(0.2989 * r + 0.5870 * g + 0.1140 * b)
    return gray

# 下載隨機動漫圖片
def download_waifu_image(filename="waifu_image.png"):
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

# 調整圖像大小並轉換為灰度
def resize_gray_image(image, new_width=150):
    width_img, height = image.size
    aspect_ratio = height / width_img
    new_height = int(aspect_ratio * new_width * 0.5)
    resized_image = image.resize((new_width, new_height))

    # 使用自定義的 RGB 到灰度轉換
    gray_image = resized_image.convert("RGB")
    grayscale_pixels = [rgb_to_grayscale(r, g, b) for r, g, b in gray_image.getdata()]
    grayscale_image = Image.new("L", resized_image.size)
    grayscale_image.putdata(grayscale_pixels)

    return grayscale_image

# 將圖像轉換為 ASCII 字符串
def image_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel * (len(ASCII_CHARS) - 1) // 255] for pixel in pixels])
    return ascii_str

# 將 ASCII 字符串繪製到圖像
def ascii_to_image(ascii_str, image_width, output_path, font_size=10, bg_color="black", font_color="white"):
    lines = [ascii_str[index: index + image_width] for index in range(0, len(ascii_str), image_width)]
    char_width = font_size * 0.6
    char_height = font_size
    img_width = int(char_width * image_width)
    img_height = int(char_height * len(lines))
    
    img = Image.new("RGB", (img_width, img_height), color=bg_color)
    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("DejaVuSansMono.ttf", size=font_size)
    except IOError:
        font = ImageFont.load_default()
        print("Could not find specified font, using default font.")
    
    y = 0
    for line in lines:
        draw.text((0, y), line, fill=font_color, font=font)
        y += char_height
    
    img.save(output_path)
    print(f"ASCII image saved as {output_path}")

# 主程序流程
output_image_path = './files/ascii_art.png'
#original_path = download_waifu_image("original.png")
#original_path = "./omuba_1.jpeg"
if original_path:
    try:
        image = Image.open(original_path)
    except Exception as e:
        print(f"Error opening image: {e}")
    else:
        # 調整圖像並轉換為灰度
        gray_image = resize_gray_image(image, new_width=1000)
        # 將灰度圖像轉換為 ASCII 字符串
        ascii_str = image_to_ascii(gray_image)
        # 將 ASCII 字符串繪製到圖像並保存
        ascii_to_image(ascii_str, gray_image.width, output_image_path, font_size=10, bg_color="black", font_color="white")

        # 顯示 ASCII 藝術圖像
        def display_image(image_path):
            root = tk.Tk()
            root.title("ASCII Art")
            
            img = Image.open(image_path)
            
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            img_width, img_height = img.size
            
            if img_width > screen_width or img_height > screen_height:
                ratio = min(screen_width / img_width, screen_height / img_height) * 0.8
                img = img.resize((int(img_width * ratio), int(img_height * ratio)), Image.LANCZOS)
            
            tk_image = ImageTk.PhotoImage(img)
            label = tk.Label(root, image=tk_image)
            label.image = tk_image
            label.pack()
            root.mainloop()
        display_image(output_image_path)
