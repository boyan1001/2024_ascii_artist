![ascii-text-art](https://github.com/user-attachments/assets/2f304d18-22df-4995-bd1f-18445d09078b)              
# 2024 ASCII ARTIST
這是一個 **ascii art** 生成器。  
  
你可以輸入照片或隨機產生照片與其互動。  
  
甚至你可以透過打開前置攝像頭互動，產生及時的 ascii art 圖像。  　

## 🧱 結構

```sh
2024_ascii_artist
├── /files/ 存放照片檔案的地方，你也可以在這邊加入你想要輸入的圖片  
│  ├── original.png  原始檔案
│  ├── modify.png  經過調整對比度與亮度處理的圖片
│  ├── ascii_art.png  轉換成 ascii_art 風格的圖片
│  └── ...
├── /font/  儲存字體的資料夾  
│  ├── DejaVuSansMono.ttf  目前正在使用在 ascii art 的字體，必須為等寬且可支援 window 環境的字體  
│  └── ...
├── main.py  主函式
├── camera.py 照相機模組  
├── UI.py  UI 函式庫  
├── .gitignore
├── LICENSE
└── README.md
```

## 🛠️ 貢獻者須知  

有任何想法，歡迎在 [Issues](https://github.com/boyan1001/boyan_csie_notebook/issues) 提出  

## 🪪 Lisence  
[MIT License](LICENSE) © Hank Chen  
