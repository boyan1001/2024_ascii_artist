![ascii-text-art](https://github.com/user-attachments/assets/2f304d18-22df-4995-bd1f-18445d09078b)       
  
![contributor](https://img.shields.io/github/contributors/boyan1001/2024_ascii_artist?style=for-the-badge)
![license](https://img.shields.io/github/license/boyan1001/2024_ascii_artist?style=for-the-badge)
![Last Commit](https://img.shields.io/github/last-commit/boyan1001/2024_ascii_artist?style=for-the-badge)
![Pull Requests](https://img.shields.io/github/issues-pr/boyan1001/2024_ascii_artist?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-14354C.svg?logo=python&logoColor=white&style=for-the-badge)
![windows](https://img.shields.io/badge/windows-0078D6?logo=windows&logoColor=white&style=for-the-badge)


本程式是**2024 師大資工白客松**中我們小隊（**歐姆巴說的對**）的參賽作品：**Ascii Artist**   

## ✨ 概述  

這是一個 **ascii art** 生成器。  
  
你可以輸入照片或隨機產生照片與其互動。  
  
甚至你可以透過打開前置攝像頭互動，產生及時的 ascii art 圖像。 

## 🧑‍💻 團隊分工  
```sh
boyan1001 (Hank Chen) : Project manager / Camera interacting function /
                        Colorful ascii art image generating / TUI design

noyapoyo : Use anime api (waifu) and dog api (dor.ceo) /
           Black and white ascii art image generating

Jerryleess : Find api we can use / Offer ideas to us   
```

## 🧱 結構

```sh
2024_ascii_artist
├── /files/                存放照片檔案的地方，你也可以在這邊加入你想要輸入的圖片  
│  ├── original.png        原始檔案
│  ├── modify.png          經過調整對比度與亮度處理的圖片
│  ├── ascii_art.png       轉換成 ascii_art 風格的圖片
│  └── ...
├── /font/                 儲存字體的資料夾  
│  ├── DejaVuSansMono.ttf  目前正在使用在 ascii art 的字體，必須為等寬且可支援 window 環境的字體  
│  └── ...
├── main.py                主函式
├── camera.py              照相機模組  
├── UI.py                  UI 函式庫  
└── ...
```
## 🖥️ 環境要求    

本程式可在 **Window** 作業系統上順利執行。  

由於 **Ascii Artist** 有使用到許多 **pip** 套件，因此必須要先安裝完所需的套件才可執行。

請先確認您所屬環境中是否已安裝 **python** 及 **pip**。  
*(Python 版本要求 : python 3.10 以上)*  
```bach
python3 --version
pip --version
```
如果你尚未安裝，請先安裝完成。  
  
接著，安裝 **requests、pillow、opencv-python、numpy** 這四個套件在您所屬的環境中：  
（為了防止套件衝突，可以使用 **虛擬環境** 安裝套件）  
```bach
pip install requests pillow opencv-python numpy
```
安裝完成套件後，即可執行該程式。  

## ⚙️ 執行程式
如果你已安裝完環境後，可輸入下方指令開始執行程式：  
```bash
python main.py
```
本程式使用 **TUI** 設計，整個程式將在 **Terminal** 中執行。  

## 🛠️ 貢獻者須知  

貢獻者需知可參考 [CONTRIBUTING.md](CONTRIBUTING.md) 與 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) 檔案～  
  
有任何想法，歡迎在 [Issues](https://github.com/boyan1001/boyan_csie_notebook/issues) 提出。  

## 💪 貢獻者
感謝下列大大們的貢獻～  
  
<a href="https://github.com/boyan1001/2024_ascii_artist/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=boyan1001/2024_ascii_artist" />
</a>
  
（可在 [**contributer**](https://github.com/boyan1001/2024_ascii_artist/graphs/contributors) 中觀看完整版貢獻者清單）  

## 🪪 Lisence  
[MIT License](LICENSE) © Hank Chen  
