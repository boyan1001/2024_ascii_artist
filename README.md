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
                        Colorful ascii art image / TUI design

noyapoyo : Use anime api (waifu) and dog api (dor.ceo) /
           Black and white ascii art image

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

## 🛠️ 貢獻者須知  

貢獻者需知可參考 [CONTRIBUTING.md](CONTRIBUTING.md) 與 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) 檔案～  
  
有任何想法，歡迎在 [Issues](https://github.com/boyan1001/boyan_csie_notebook/issues) 提出  

## 💪 貢獻者
感謝下列大大們的貢獻～  
  
<a href="https://github.com/boyan1001/2024_ascii_artist/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=boyan1001/2024_ascii_artist" />
</a>


## 🪪 Lisence  
[MIT License](LICENSE) © Hank Chen  
