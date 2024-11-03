import cv2
import numpy as np

ASCII_CHARS = "@%#*+=-:. "

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

# 開啟攝像頭
cap = cv2.VideoCapture(0)

try:
    while True:
        # 讀取攝像頭幀
        ret, frame = cap.read()
        if not ret:
            break

        # 將幀轉換為 ASCII 藝術並輸出到終端
        ascii_art = image_to_ascii(frame, width=100)
        print("\033c", end="")  # 清空終端
        print(ascii_art)

        # 停頓短暫時間以達到即時效果
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    # 釋放攝像頭資源
    cap.release()
    cv2.destroyAllWindows()