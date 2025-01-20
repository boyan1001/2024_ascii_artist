import cv2
import numpy as np
import threading

exit_flag = False

def find_camera_id():
    for camera_id in range(10):
        cap = cv2.VidoeCapture(camera_id)
        if cap.isOpened():
            cap.release()
            return camera_id
    return -1

def camera_mode():
    global exit_flag
    exit_flag = False

    # ascii art generator
    ASCII_CHARS = " .',:;\"^`i!lI><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQO0Zmwpqdbkhao*#MW&8%B@$"

    def image_to_ascii(frame, width=100):
        # modifiy frame
        aspect_ratio = frame.shape[0] / frame.shape[1]
        height = int(aspect_ratio * width * 0.5)
        resized_gray_frame = cv2.resize(frame, (width, height))
        gray_frame = cv2.cvtColor(resized_gray_frame, cv2.COLOR_BGR2GRAY)

        # chage to ascii
        ascii_frame = ""
        for pixel in gray_frame.flatten():
            ascii_frame += ASCII_CHARS[pixel // 32]

        ascii_lines = [ascii_frame[i:i + width] for i in range(0, len(ascii_frame), width)]
        return "\n".join(ascii_lines)

    def wait_for_enter():
        global exit_flag
        input("Press Enter to stop...\n")
        exit_flag = True

    # open camera
    camera_id = find_camera_id()

    if camera_id == -1:
        print("Cannot find camera")
        return
    
    cap = cv2.VideoCapture(camera_id)

    # start thread
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

            # 水平翻轉幀
            frame = cv2.flip(frame, 1)

            # 將幀轉換為 ASCII 藝術並輸出到終端
            ascii_art = image_to_ascii(frame, width=100)
            print("\033c", end="")  # 清空終端
            print(ascii_art)

            # exit
            if exit_flag:
                break

    finally:
        print("\033[?25h", end="")  

        cap.release()
        cv2.destroyAllWindows()
        print("程序已停止")
        return
