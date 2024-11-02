from PIL import Image

# 定义图片尺寸
width, height = 256, 256

# 创建一张新的 RGB 图片
image = Image.new('RGB', (width, height))

# 遍历每个像素位置并设置像素值
for y in range(height):
    for x in range(width):
        gray_value = x  # x 从 0 到 255 递增
        image.putpixel((x, y), (gray_value, gray_value, gray_value))

# 保存图片到文件
image.save('gradient_image.png')
