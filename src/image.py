import os
from io import BytesIO
from PIL import Image, ImageEnhance, ImageDraw, ImageFont, ImageTk
import tkinter as tk


# display original image
def display_original_image(image):
    root = tk.Tk()
    root.title("Original Image")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    img_width, img_height = image.size

    if img_width > screen_width or img_height > screen_height:
        ratio = min(screen_width / img_width, screen_height / img_height) * 0.8
        image_resized = image.resize((int(img_width * ratio), int(img_height * ratio)), Image.LANCZOS)
    else:
        image_resized = image

    tk_image = ImageTk.PhotoImage(image_resized)

    label = tk.Label(root, image=tk_image)
    label.image = tk_image
    label.pack()

    root.mainloop()

def modify_image(image, modify_path):
    # 增加對比度
    contrast_enhancer = ImageEnhance.Contrast(image)
    image_contrasted = contrast_enhancer.enhance(1.2)  # original = 1.0

    # 降低亮度
    brightness_enhancer = ImageEnhance.Brightness(image_contrasted)
    image_result = brightness_enhancer.enhance(1.5)  # original = 1.0

    image_result.save(modify_path)


# ascii art generator
ASCII_CHARS = " .',:;\"^`i!lI><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQO0Zmwpqdbkhao*#MW&8%B@$"

# 將 RGB 值轉換為灰度值
def rgb_to_grayscale(r, g, b):
    gray = int(0.2989 * r + 0.5870 * g + 0.1140 * b)
    return gray

def black_gray_image(image, new_width=150):

    # 使用自定義的 RGB 到灰度轉換
    gray_image = image.convert("RGB")
    grayscale_pixels = [rgb_to_grayscale(r, g, b) for r, g, b in gray_image.getdata()]
    grayscale_image = Image.new("L", image.size)
    grayscale_image.putdata(grayscale_pixels)

    return grayscale_image

def resize_image(image, new_width=150):
    width_img, height = image.size
    aspect_ratio = height / width_img
    new_height = int(aspect_ratio * new_width * 0.5)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def black_image_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel * (len(ASCII_CHARS) - 1) // 255] for pixel in pixels])
    return ascii_str

def black_ascii_to_image(ascii_str, image_width, output_path, font_size=10, bg_color="black", font_color="white"):

    lines = [ascii_str[index: index + image_width] for index in range(0, len(ascii_str), image_width)]
    char_width = font_size * 0.6
    char_height = font_size
    img_width = int(char_width * image_width)
    img_height = int(char_height * len(lines))
    
    img = Image.new("RGB", (img_width, img_height), color=bg_color)
    draw = ImageDraw.Draw(img)
    
    # load a font
    try:
        
        font = ImageFont.truetype("./docs/font/DejaVuSansMono.ttf", size=font_size)  # for Linux 
    except IOError:
        try:
            font = ImageFont.truetype("Consolas.ttf", size=font_size)  # for Windows 
        except IOError:
            try:
                font = ImageFont.truetype("Lucida Console.ttf", size=font_size)  # for Windows
            except IOError:
                font = ImageFont.load_default()  # original font
                print("Unable to find the specified font, using the default font.")
    
    y = 0
    for line in lines:
        draw.text((0, y), line, fill=font_color, font=font)
        y += char_height
    
    img.save(output_path)
    print(f"ASCII 图像已保存为 {output_path}")

# 將圖像轉換為 ASCII 字符串，同時保留顏色資訊
def image_to_ascii(image):
    pixels = image.getdata()
    ascii_chars = []
    colors = []
    for pixel in pixels:
        r, g, b = pixel[:3]  # 獲取 RGB 值
        gray = int(0.2989 * r + 0.5870 * g + 0.1140 * b)
        ascii_char = ASCII_CHARS[gray * (len(ASCII_CHARS) - 1) // 255]
        ascii_chars.append(ascii_char)
        colors.append((r, g, b))
    ascii_str = ''.join(ascii_chars)
    return ascii_str, colors

def ascii_to_image(ascii_str, colors, image_width, output_path, font_size=10, bg_color="black"):
    # 计算图像的宽度和高度
    lines = [ascii_str[index: index + image_width] for index in range(0, len(ascii_str), image_width)]
    line_colors = [colors[index: index + image_width] for index in range(0, len(colors), image_width)]
    char_width = font_size * 0.6  # 字符的宽度，可能需要根据字体调整
    char_height = font_size
    img_width = int(char_width * image_width)
    img_height = int(char_height * len(lines))
    
    # 创建新的图像
    img = Image.new("RGB", (img_width, img_height), color=bg_color)
    draw = ImageDraw.Draw(img)
    
    # 加載等寬字體
    try:
        # 嘗試在不同系統上使用常見的等寬字體
        font = ImageFont.truetype("./docs/font/DejaVuSansMono.ttf", size=font_size)
    except IOError:
        try:
            font = ImageFont.truetype("Consolas.ttf", size=font_size)
        except IOError:
            try:
                font = ImageFont.truetype("Lucida Console.ttf", size=font_size)
            except IOError:
                font = ImageFont.load_default()
                print("无法找到指定字体，使用默认字体。")
    
    # 绘制每一行
    y = 0
    for line_num, line in enumerate(lines):
        x = 0
        for char_num, char in enumerate(line):
            color = line_colors[line_num][char_num]
            draw.text((x, y), char, fill=color, font=font)
            x += char_width
        y += char_height
    
    # 保存图像
    img.save(output_path)
    print(f"ASCII 图像已保存为 {output_path}")


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