import cv2
import numpy as np
import threading

# 定義一個全局變量，用於退出標誌
exit_flag = False

def camera_mode():
    # ASCII 字符集，用於生成 ASCII 藝術
    ASCII_CHARS = " .',:;\"^`i!lI><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQO0Zmwpqdbkhao*#MW&8%B@$"

    def image_to_ascii(frame, width=100):
        # 調整圖像大小
        aspect_ratio = frame.shape[0] / frame.shape[1]
        height = int(aspect_ratio * width * 0.5)  # 調整高度比例
        resized_gray_frame = cv2.resize(frame, (width, height))
        gray_frame = cv2.cvtColor(resized_gray_frame, cv2.COLOR_BGR2GRAY)

        # 將每個像素轉換為 ASCII 字符
        ascii_frame = ""
        for pixel in gray_frame.flatten():
            ascii_frame += ASCII_CHARS[pixel // 32]
        
        # 格式化 ASCII 字符串以進行顯示
        ascii_lines = [ascii_frame[i:i + width] for i in range(0, len(ascii_frame), width)]
        return "\n".join(ascii_lines)

    def wait_for_enter():
        global exit_flag
        input("Press Enter to stop...\n")
        exit_flag = True

    # 開啟攝像頭
    cap = cv2.VideoCapture(0)

    # 啟動監聽 Enter 鍵的執行緒
    thread = threading.Thread(target=wait_for_enter)
    thread.start()

    try:
        # 隱藏游標
        print("\033[?25l", end="")
        while True:
            # 讀取攝像頭幀
            ret, frame = cap.read()
            if not ret or exit_flag:
                break

            # 將幀轉換為 ASCII 藝術並輸出到終端
            ascii_art = image_to_ascii(frame, width=100)
            print("\033c", end="")  # 清空終端
            print(ascii_art)
            # print("\n\nPress Enter to stop...")

    finally:
        print("\033[?25h", end="")
        # 釋放攝像頭資源
        cap.release()
        cv2.destroyAllWindows()
        print("程序已停止")
        return