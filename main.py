from PIL import Image, ImageEnhance, ImageDraw, ImageFont

width = 350

# 原始图像路径
jpg_path = './assert/test3.png'
image_path = './temp.png'

# 打开图像
image = Image.open(jpg_path)

# 增加对比度
contrast_enhancer = ImageEnhance.Contrast(image)
image_contrasted = contrast_enhancer.enhance(1.8)  # 1.0 为原始值，大于 1.0 增加对比度

# 降低亮度
brightness_enhancer = ImageEnhance.Brightness(image_contrasted)
image_result = brightness_enhancer.enhance(0.9)  # 1.0 为原始值，小于 1.0 降低亮度

# 保存临时处理后的图像
image_result.save(image_path)

# ASCII 字符集，包含更多字符以获得更好的效果
ASCII_CHARS = "@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%############################*****************************++++++++++++++++++++++++++++============================-----------------------------::::::::::::::::::::::::::::............................               "

def resize_gray_image(image, new_width = width):
    width, height = image.size
    aspect_ratio = height / width
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
