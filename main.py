import requests
import os
from io import BytesIO
from PIL import Image, ImageEnhance, ImageDraw, ImageFont, ImageTk
import tkinter as tk

import src.UI as UI
import src.camera as cam
import src.api as api
import src.image as im

# paths
original_path = './docs/files/original.png'
modify_path = './docs/files/modify.png'

# picture size
width = 500


while (True):
    UI.clear()
    UI.title()
    print("Welcome to the ASCII ART Generator!")
    print("\nWhat kind of image would you like to convert to ASCII art?")
    print("1. Random Anime Image")
    print("2. Random Dog Image")
    print("3. Your Image")
    print("4. Camera Mode")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    # 原始图像路径
    original_path = './docs/files/original.png'
    modify_path = './docs/files/modify.png'


    # 判斷用戶選擇
    if choice == "1": # 隨機動漫圖片
        UI.clear()
        UI.title()

        # 打開圖片
        api.download_waifu_image("./docs/files/original.png")
        image = Image.open(original_path)
        im.display_original_image(image)

        # 調整圖片大小
        image = im.resize_image(image, new_width=width)

        while True:
            print("Choose a feature you want to generate:")
            print("1. Colorful Image")
            print("2. Black and White Image")
            print("3. Exit")
            choise = input("Enter your choice (1/2/3): ")
            
            if choise == "1":

                im.modify_image(image, modify_path)

                # 將圖像轉換為 ASCII 字符串和顏色
                ascii_str, colors = im.image_to_ascii(image)
                output_image_path = "./docs/files/ascii_art.png"


                # 將 ASCII 字符串繪製到圖像並保存（帶顏色）
                im.ascii_to_image(ascii_str, colors, image.width, output_image_path, font_size=10, bg_color="black")
                # 顯示 ASCII 藝術圖像
                im.display_image(output_image_path)

            elif choise == "2":

                # 調整圖片
                im.modify_image(image, modify_path)

                # 調整圖像並轉換為灰度
                gray_image = im.black_gray_image(image, new_width=width)
                # 將灰度圖像轉換為ASCII字符串
                ascii_str = im.black_image_to_ascii(gray_image)
                output_image_path = "./docs/files/ascii_art.png"
                # 將ASCII字符串繪製到圖像並保存
                im.black_ascii_to_image(ascii_str, gray_image.width, output_image_path)
                # 顯示ASCII藝術圖像
                im.display_image(output_image_path)

            else:
                break

        continue

    elif choice == "2": # 隨機狗狗圖片
        UI.clear()
        UI.title()

        # 打開圖片
        api.download_dog_image("./docs/files/original.png")
        image = Image.open(original_path)
        im.display_original_image(image)

        # 調整圖片大小
        image = im.resize_image(image, new_width=width)

        while True:
            print("Choose a feature you want to generate:")
            print("1. Colorful Image")
            print("2. Black and White Image")
            print("3. Exit")
            choise = input("Enter your choice (1/2/3): ")
            
            if choise == "1":

                im.modify_image(image, modify_path)

                # 將圖像轉換為 ASCII 字符串和顏色
                ascii_str, colors = im.image_to_ascii(image)
                output_image_path = "./docs/files/ascii_art.png"


                # 將 ASCII 字符串繪製到圖像並保存（帶顏色）
                im.ascii_to_image(ascii_str, colors, image.width, output_image_path, font_size=10, bg_color="black")
                # 顯示 ASCII 藝術圖像
                im.display_image(output_image_path)

            elif choise == "2":

                # 調整圖片
                im.modify_image(image, modify_path)

                # 調整圖像並轉換為灰度
                gray_image = im.black_gray_image(image, new_width=width)
                # 將灰度圖像轉換為ASCII字符串
                ascii_str = im.black_image_to_ascii(gray_image)
                output_image_path = "./docs/files/ascii_art.png"
                # 將ASCII字符串繪製到圖像並保存
                im.black_ascii_to_image(ascii_str, gray_image.width, output_image_path)
                # 顯示ASCII藝術圖像
                im.display_image(output_image_path)

            else:
                break

        continue

    elif choice == "3": # 用戶自己的圖片
        while True:
            UI.clear()
            UI.title()
            print("Please check the files in the /files folder")
            original_path = "./docs/files/" + input("Enter the image file name: ")
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
        im.display_original_image(image)

        # 調整圖片大小
        image = im.resize_image(image, new_width=width)

        while True:
            print("Choose a feature you want to generate:")
            print("1. Colorful Image")
            print("2. Black and White Image")
            print("3. Exit")
            choise = input("Enter your choice (1/2/3): ")
            
            if choise == "1":

                im.modify_image(image, modify_path)

                # 將圖像轉換為 ASCII 字符串和顏色
                ascii_str, colors = im.image_to_ascii(image)
                output_image_path = "./docs/files/ascii_art.png"


                # 將 ASCII 字符串繪製到圖像並保存（帶顏色）
                im.ascii_to_image(ascii_str, colors, image.width, output_image_path, font_size=10, bg_color="black")
                # 顯示 ASCII 藝術圖像
                im.display_image(output_image_path)

            elif choise == "2":

                # 調整圖片
                im.modify_image(image, modify_path)

                # 調整圖像並轉換為灰度
                gray_image = im.black_gray_image(image, new_width=width)
                # 將灰度圖像轉換為ASCII字符串
                ascii_str = im.black_image_to_ascii(gray_image)
                output_image_path = "./docs/files/ascii_art.png"
                # 將ASCII字符串繪製到圖像並保存
                im.black_ascii_to_image(ascii_str, gray_image.width, output_image_path)
                # 顯示ASCII藝術圖像
                im.display_image(output_image_path)

            else:
                break

        continue

    elif choice == "4": # 照相機功能
        UI.clear()
        cam.camera_mode()
        continue

    elif choice == "5": # 退出
        UI.clear()
        UI.title()
        print("Goodbye!")
        break