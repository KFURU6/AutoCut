# PDFから文字や表を取り出すためのライブラリ
import pdfplumber

# 正規表現（文字パターン検索）
import re

# 記号ごとに保存する辞書
values = {
    "L": [],
    "□": [],
    "C": [],
    "FB": []
}

# PDFを開く
with pdfplumber.open("sample.pdf") as pdf:

    # 1ページずつ処理
    for page in pdf.pages:

        # テキスト抽出
        text = page.extract_text()

        if text:

            # L + 数字
            l_numbers = re.findall(r'L\s*(\d+)', text)
            values["L"].extend(l_numbers)

            # □ + 数字
            square_numbers = re.findall(r'□\s*(\d+)', text)
            values["□"].extend(square_numbers)

            # C + 数字
            c_numbers = re.findall(r'C\s*(\d+)', text)
            values["C"].extend(c_numbers)

            # FB + 数字
            fb_numbers = re.findall(r'FB\s*(\d+)', text)
            values["FB"].extend(fb_numbers)

# 結果表示
print(values)