import requests
import os
from PIL import Image, ImageEnhance, ImageDraw, ImageFont, ImageTk
import tkinter as tk

# 原始图像路径
jpg_path = './temp.png'
image_path = jpg_path

# 照片尺寸
width = 500

# 发出请求并获取图片 URL
response = requests.get('https://dog.ceo/api/breeds/image/random')

if response.status_code == 200:
    data = response.json()
    image_url = data.get('message')
    print(f"图片的 URL 是：{image_url}")

    # 下载图片
    image_response = requests.get(image_url)
    if image_response.status_code == 200:
        # 保存图片
        with open(jpg_path, 'wb') as file:
            file.write(image_response.content)
        print(f"图片已保存为 {jpg_path}")
    else:
        print(f"无法下载图片。状态码：{image_response.status_code}")
else:
    print(f"无法获取数据。状态码：{response.status_code}")

# 打开图像
image = Image.open(jpg_path)

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

# 调用显示原始图像的函数
display_original_image(image)

# 增加对比度
contrast_enhancer = ImageEnhance.Contrast(image)
image_contrasted = contrast_enhancer.enhance(1.5)  # 1.0 为原始值，大于 1.0 增加对比度

# 降低亮度
brightness_enhancer = ImageEnhance.Brightness(image_contrasted)
image_result = brightness_enhancer.enhance(0.8)  # 1.0 为原始值，小于 1.0 降低亮度

# 保存处理后的图像
image_result.save(image_path)

# ASCII 字符集，包含更多字符以获得更好的效果
ASCII_CHARS = "@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%############################*****************************++++++++++++++++++++++++++++============================-----------------------------::::::::::::::::::::::::::::............................               "

def resize_gray_image(image, new_width=width):
    width_img, height = image.size
    aspect_ratio = height / width_img
    new_height = int(aspect_ratio * new_width * 0.5)  # 调整高度以匹配字符的宽高比
    resized_image = image.resize((new_width, new_height))
    gray_image = resized_image.convert("L")  # 转换为灰度图像
    return gray_image

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

# 主程序
output_image_path = 'ascii_art.png'

try:
    image = Image.open(image_path)
except Exception as e:
    print(f"Error opening image: {e}")
else:
    # 调整图像并转换为灰度
    gray_image = resize_gray_image(image, new_width=width)
    # 将灰度图像转换为 ASCII 字符串
    ascii_str = image_to_ascii(gray_image)
    # 将 ASCII 字符串绘制到图像并保存
    ascii_to_image(ascii_str, gray_image.width, output_image_path, font_size=10, bg_color="black", font_color="white")

    # 显示 ASCII 艺术图像
    def display_image(image_path):
        root = tk.Tk()
        root.title("ASCII Art")
        
        # 打开图像文件
        img = Image.open(image_path)
        
        # 调整图像大小以适应屏幕
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        img_width, img_height = img.size
        
        if img_width > screen_width or img_height > screen_height:
            ratio = min(screen_width / img_width, screen_height / img_height) * 0.8  # 缩放到屏幕的 80%
            img = img.resize((int(img_width * ratio), int(img_height * ratio)), Image.LANCZOS)
        
        # 将图像转换为 Tkinter 可显示的格式
        tk_image = ImageTk.PhotoImage(img)
        
        # 创建标签来显示图像
        label = tk.Label(root, image=tk_image)
        label.image = tk_image  # 保持引用，防止被垃圾回收
        label.pack()
        
        # 启动 Tkinter 主循环
        root.mainloop()
    
    # 调用显示 ASCII 艺术图像的函数
    display_image(output_image_path)
