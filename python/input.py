# 以下コマンドでlocalにクローン
# cd C:\Users\kanta\OneDrive\Desktop
# rmdir /s /q AutoCut
# git clone https://github.com/KFURU6/AutoCut.git
# cd C:\Users\kanta\OneDrive\Desktop\AutoCut\python\
# python .\output.py


# PDFから文字や表を取り出す
import pdfplumber

# 正規表現
import re

# 規格データ
data = [
    # L形鋼
    {"shape": "L", "thickness": 3, "width": 30, "height": 30, "length": None},
    {"shape": "L", "thickness": 3, "width": 40, "height": 40, "length": None},
    {"shape": "L", "thickness": 4, "width": 50, "height": 50, "length": None},
    {"shape": "L", "thickness": 6, "width": 50, "height": 50, "length": None},
    {"shape": "L", "thickness": 6, "width": 65, "height": 65, "length": None},
    {"shape": "L", "thickness": 6, "width": 75, "height": 75, "length": None},

    # 角パイプ（□）
    {"shape": "□", "thickness": 1.6, "width": 25, "height": 25, "length": None},
    {"shape": "□", "thickness": 1.6, "width": 31, "height": 31, "length": None},
    {"shape": "□", "thickness": 1.6, "width": 40, "height": 40, "length": None},
    {"shape": "□", "thickness": 2.3, "width": 50, "height": 50, "length": None},
    {"shape": "□", "thickness": 2.3, "width": 45, "height": 75, "length": None},
    {"shape": "□", "thickness": 2.3, "width": 50, "height": 100, "length": None},
    {"shape": "□", "thickness": 3.2, "width": 75, "height": 125, "length": None},

    # チャンネル（C）
    {"shape": "C", "thickness": 5, "width": 40, "height": 75, "length": None},
    {"shape": "C", "thickness": 5, "width": 50, "height": 100, "length": None},
    {"shape": "C", "thickness": 6, "width": 65, "height": 125, "length": None},
    {"shape": "C", "thickness": 6.5, "width": 75, "height": 150, "length": None},
    {"shape": "C", "thickness": 8, "width": 90, "height": 200, "length": None},

    # フラットバー（FB）
    {"shape": "FB", "thickness": 3, "width": 32, "height": 3, "length": None},
    {"shape": "FB", "thickness": 4.5, "width": 44, "height": 4.5, "length": None},
    {"shape": "FB", "thickness": 6, "width": 90, "height": 6, "length": None},
    {"shape": "FB", "thickness": 9, "width": 100, "height": 9, "length": None},
    {"shape": "FB", "thickness": 19, "width": 75, "height": 19, "length": None},
]

# 一致した結果
matched = []

# PDFを開く
with pdfplumber.open("sample.pdf") as pdf:

    for page in pdf.pages:

        text = page.extract_text()

        if not text:
            continue

        # ------------------------
        # L形鋼
        # 例: L 50x50x6
        # ------------------------
        l_matches = re.findall(
            r'L\s*(\d+)x(\d+)x([\d\.]+)',
            text
        )

        for w1, w2, t in l_matches:

            width = int(w1)
            thickness = float(t)

            for item in data:
                if (
                    item["shape"] == "L"
                    and item["width"] == width
                    and item["thickness"] == thickness
                ):
                    matched.append(item)

        # ------------------------
        # 角パイプ
        # 例: □50x100x2.3
        # ------------------------
        square_matches = re.findall(
            r'□\s*(\d+)x(\d+)x([\d\.]+)',
            text
        )

        for w, h, t in square_matches:

            width = int(w)
            height = int(h)
            thickness = float(t)

            for item in data:
                if (
                    item["shape"] == "□"
                    and item["width"] == width
                    and item["height"] == height
                    and item["thickness"] == thickness
                ):
                    matched.append(item)

        # ------------------------
        # Cチャンネル
        # 例: C 75x40x5
        # ------------------------
        c_matches = re.findall(
            r'C\s*(\d+)x(\d+)x([\d\.]+)',
            text
        )

        for h, w, t in c_matches:

            width = int(w)
            height = int(h)
            thickness = float(t)

            for item in data:
                if (
                    item["shape"] == "C"
                    and item["width"] == width
                    and item["height"] == height
                    and item["thickness"] == thickness
                ):
                    matched.append(item)

        # ------------------------
        # FB
        # 例: FB 90x6
        # ------------------------
        fb_matches = re.findall(
            r'FB\s*(\d+)x([\d\.]+)',
            text
        )

        for w, t in fb_matches:

            width = int(w)
            thickness = float(t)

            for item in data:
                if (
                    item["shape"] == "FB"
                    and item["width"] == width
                    and item["thickness"] == thickness
                ):
                    matched.append(item)

# 表示
print("一致した規格:")
for item in matched:
    print(item)