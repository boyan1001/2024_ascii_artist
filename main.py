import requests
import os
from io import BytesIO
from PIL import Image, ImageEnhance, ImageDraw, ImageFont, ImageTk
import tkinter as tk
import UI

# 原始图像路径
original_path = './files/original.png'
modify_path = './files/modify.png'

# 照片尺寸
width = 500

# 下载一张随机的动漫图片

def download_waifu_image(filename=original_path):
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

# 从 API 下载一张狗狗的图片
# 发出请求并获取图片 URL
def download_dog_image(image_path):
    response = requests.get('https://dog.ceo/api/breeds/image/random')

    if response.status_code == 200:
        data = response.json()
        image_url = data.get('message')
        print(f"圖片的 URL：{image_url}")

        # 下载图片
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            # 保存图片
            with open(image_path, 'wb') as file:
                file.write(image_response.content)
            print(f"圖片已保存到 {image_path}")
        else:
            print(f"無法下載圖片，狀態碼：{image_response.status_code}")
    else:
        print(f"無法獲取數據，狀態碼：{response.status_code}")
    return image_path

# 显示原始图像
def display_original_image(image):
    root = tk.Tk()
    root.title("Original Image")

    # 调整图像大小以适应屏幕
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    img_width, img_height = image.size

    if img_width > screen_width or img_height > screen_height:
        ratio = min(screen_width / img_width, screen_height / img_height) * 0.8  # 缩放到屏幕的 80%
        image_resized = image.resize((int(img_width * ratio), int(img_height * ratio)), Image.LANCZOS)
    else:
        image_resized = image

    # 将图像转换为 Tkinter 可显示的格式
    tk_image = ImageTk.PhotoImage(image_resized)

    # 创建标签来显示图像
    label = tk.Label(root, image=tk_image)
    label.image = tk_image  # 保持引用，防止被垃圾回收
    label.pack()

    # 启动 Tkinter 主循环
    root.mainloop()

def modify_image():
    # 增加对比度
    contrast_enhancer = ImageEnhance.Contrast(image)
    image_contrasted = contrast_enhancer.enhance(1.0)  # 1.0 为原始值，大于 1.0 增加对比度

    # 降低亮度
    brightness_enhancer = ImageEnhance.Brightness(image_contrasted)
    image_result = brightness_enhancer.enhance(1.0)  # 1.0 为原始值，小于 1.0 降低亮度

    # 保存处理后的图像
    image_result.save(modify_path)


# ASCII 字符集，用於生成 ASCII 藝術
ASCII_CHARS = " .',:;\"^`i!lI><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQO0Zmwpqdbkhao*#MW&8%B@$"

# 將 RGB 值轉換為灰度值
def rgb_to_grayscale(r, g, b):
    gray = int(0.2989 * r + 0.5870 * g + 0.1140 * b)
    return gray

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

def image_to_ascii(image):
    pixels = image.getdata()
    # 将像素值映射到 ASCII 字符集的索引范围内
    ascii_str = "".join([ASCII_CHARS[pixel * (len(ASCII_CHARS) - 1) // 255] for pixel in pixels])
    return ascii_str

def ascii_to_image(ascii_str, image_width, output_path, font_size=10, bg_color="black", font_color="white"):
    # 计算图像的宽度和高度
    lines = [ascii_str[index: index + image_width] for index in range(0, len(ascii_str), image_width)]
    char_width = font_size * 0.6  # 字符的宽度，可能需要根据字体调整
    char_height = font_size
    img_width = int(char_width * image_width)
    img_height = int(char_height * len(lines))
    
    # 创建新的图像
    img = Image.new("RGB", (img_width, img_height), color=bg_color)
    draw = ImageDraw.Draw(img)
    
    # 使用等宽字体，确保字符对齐
    try:
        font = ImageFont.truetype("DejaVuSansMono.ttf", size=font_size)
    except IOError:
        font = ImageFont.load_default()
        print("无法找到指定字体，使用默认字体。")
    
    # 绘制每一行
    y = 0
    for line in lines:
        draw.text((0, y), line, fill=font_color, font=font)
        y += char_height
    
    # 保存图像
    img.save(output_path)
    print(f"ASCII 图像已保存为 {output_path}")

# def generate_ascii_art(input_image_path, output_image_path, width=100, font_size=10, bg_color="black", font_color="white"):
#     def resize_gray_image(image, new_width):
#         width, height = image.size
#         aspect_ratio = height / width
#         new_height = int(aspect_ratio * new_width)
#         resized_image = image.resize((new_width, new_height))
#         gray_image = resized_image.convert("L")  # 轉換為灰度
#         return gray_image

#     def image_to_ascii(gray_image):
#         ASCII_CHARS = "@%#*+=-:. "  # ASCII字符集，用來表示不同灰度級
#         ascii_str = ""
#         pixels = gray_image.getdata()
#         for pixel in pixels:
#             ascii_str += ASCII_CHARS[pixel // 32]  # 將灰度值映射到ASCII字符
#         ascii_str = "\n".join([ascii_str[i:i + gray_image.width] for i in range(0, len(ascii_str), gray_image.width)])
#         return ascii_str

#     def ascii_to_image(ascii_str, width, output_path, font_size=10, bg_color="black", font_color="white"):
#         from PIL import Image, ImageDraw, ImageFont

#         lines = ascii_str.splitlines()
#         height = font_size * len(lines)
        
#         # 建立圖像
#         img = Image.new("RGB", (width * font_size, height), bg_color)
#         draw = ImageDraw.Draw(img)
        
#         # 使用系統默認字體
#         try:
#             font = ImageFont.truetype("arial.ttf", font_size)
#         except IOError:
#             font = ImageFont.load_default()

#         # 將ASCII字符繪製到圖像上
#         y = 0
#         for line in lines:
#             draw.text((0, y), line, font=font, fill=font_color)
#             y += font_size

#         img.save(output_path)

def display_image(image_path):
    root = tk.Tk()
    root.title("ASCII Art")
    
    # 打開圖像文件
    img = Image.open(image_path)
    
    # 調整圖像大小以適應屏幕
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    img_width, img_height = img.size
    
    if img_width > screen_width or img_height > screen_height:
        ratio = min(screen_width / img_width, screen_height / img_height) * 0.8  # 縮放到屏幕的 80%
        img = img.resize((int(img_width * ratio), int(img_height * ratio)), Image.LANCZOS)
    
    # 將圖像轉換為Tkinter可顯示的格式
    tk_image = ImageTk.PhotoImage(img)
    
    # 創建標籤來顯示圖像
    label = tk.Label(root, image=tk_image)
    label.image = tk_image  # 保持引用，防止被垃圾回收
    label.pack()
    
    # 啟動Tkinter主循環
    root.mainloop()

#     try:
#         image = Image.open(input_image_path)
#     except Exception as e:
#         print(f"Error opening image: {e}")
#     else:
#         # 調整圖像並轉換為灰度
#         gray_image = resize_gray_image(image, new_width=width)
#         # 將灰度圖像轉換為ASCII字符串
#         ascii_str = image_to_ascii(gray_image)
#         # 將ASCII字符串繪製到圖像並保存
#         ascii_to_image(ascii_str, gray_image.width, output_image_path, font_size=font_size, bg_color=bg_color, font_color=font_color)
#         # 顯示ASCII藝術圖像
#         display_image(output_image_path)

while (True):
    UI.clear()
    UI.title()
    print("Welcome to the ASCII ART Generator!")
    print("\nWhat kind of image would you like to convert to ASCII art?")
    print("1. Random Anime Image")
    print("2. Random Dog Image")
    print("3. Your Image")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    # 原始图像路径
    original_path = './files/original.png'
    modify_path = './files/modify.png'


    # 判斷用戶選擇
    if choice == "1": # 隨機動漫圖片
        UI.clear()
        UI.title()
        download_waifu_image("./files/original.png")

        # 打開圖片
        image = Image.open(original_path)
        display_original_image(image)

        # 調整圖片
        modify_image()

        # 調整圖像並轉換為灰度
        gray_image = resize_gray_image(image, new_width=width)
        # 將灰度圖像轉換為ASCII字符串
        ascii_str = image_to_ascii(gray_image)
        output_image_path = "./files/ascii_art.png"
        # 將ASCII字符串繪製到圖像並保存
        ascii_to_image(ascii_str, gray_image.width, output_image_path)
        # 顯示ASCII藝術圖像
        display_image(output_image_path)

        continue

    elif choice == "2": # 隨機狗狗圖片
        UI.clear()
        UI.title()
        download_dog_image("./files/original.png")

        # 打開圖片
        image = Image.open(original_path)
        display_original_image(image)

        # 調整圖片
        modify_image()

        # 調整圖像並轉換為灰度
        gray_image = resize_gray_image(image, new_width=width)
        # 將灰度圖像轉換為ASCII字符串
        ascii_str = image_to_ascii(gray_image)
        output_image_path = "./files/ascii_art.png"
        # 將ASCII字符串繪製到圖像並保存
        ascii_to_image(ascii_str, gray_image.width, output_image_path)
        # 顯示ASCII藝術圖像
        display_image(output_image_path)

        continue

    elif choice == "3": # 用戶自己的圖片
        while True:
            UI.clear()
            UI.title()
            print("Please check the files in the /files folder")
            original_path = "./files/" + input("Enter the image file name: ")
            ## 檢查文件是否存在
            if not os.path.exists(original_path):
                print("File not found.")
                continue
            else:
                break

        UI.clear()
        UI.title()
        
        # 打開圖片
        image = Image.open(original_path)
        display_original_image(image)

        # 調整圖片
        modify_image()

        # 調整圖像並轉換為灰度
        gray_image = resize_gray_image(image, new_width=width)
        # 將灰度圖像轉換為ASCII字符串
        ascii_str = image_to_ascii(gray_image)
        output_image_path = "./files/ascii_art.png"
        # 將ASCII字符串繪製到圖像並保存
        ascii_to_image(ascii_str, gray_image.width, output_image_path)
        # 顯示ASCII藝術圖像
        display_image(output_image_path)
        continue

    elif choice == "4": # 退出
        UI.clear()
        UI.title()
        print("Goodbye!")
        break