import os

# UI 界面
def title():
    print("                       _  _                   _    _       _   ")
    print("     /\               (_)(_)     /\          | |  (_)     | |  ")
    print("    /  \    ___   ___  _  _     /  \    _ __ | |_  _  ___ | |_ ")
    print("   / /\ \  / __| / __|| || |   / /\ \  | '__|| __|| |/ __|| __|")
    print("  / ____ \ \__ \| (__ | || |  / ____ \ | |   | |_ | |\__ \| |_ ")
    print(" /_/    \_\|___/ \___||_||_| /_/    \_\|_|    \__||_||___/ \__|")
    print("---------------------------------------------------------------")
    return

# 清空 terminal
def clear():
    # 判斷作業系統並執行相應的指令
    if os.name == 'posix':  # Linux 和 macOS
        os.system('clear')
    elif os.name == 'nt':  # Windows
        os.system('cls')
    return