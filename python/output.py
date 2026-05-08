import re
from collections import Counter

text = "A=1000 B=500 C=1000 D=500 E=250"

# 各鋼材のリスト
data = [
    # L形鋼
    {"shape": "L", "thickness": 3, "width": 30, "height": None, "length": None},
    {"shape": "L", "thickness": 3, "width": 40, "height": None, "length": None},
    {"shape": "L", "thickness": 4, "width": 50, "height": None, "length": None},
    {"shape": "L", "thickness": 6, "width": 50, "height": None, "length": None},
    {"shape": "L", "thickness": 6, "width": 65, "height": None, "length": None},
    {"shape": "L", "thickness": 6, "width": 75, "height": None, "length": None},

    # 角パイプ（□）
    {"shape": "□", "thickness": 1.6, "width": 25, "height": None, "length": None},
    {"shape": "□", "thickness": 1.6, "width": 31, "height": None, "length": None},
    {"shape": "□", "thickness": 1.6, "width": 40, "height": None, "length": None},
    {"shape": "□", "thickness": 2.3, "width": 50, "height": None, "length": None},
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
    {"shape": "FB", "thickness": 3, "width": 32, "height": None, "length": None},
    {"shape": "FB", "thickness": 4.5, "width": 44, "height": None, "length": None},
    {"shape": "FB", "thickness": 6, "width": 90, "height": None, "length": None},
    {"shape": "FB", "thickness": 9, "width": 100, "height": None, "length": None},
    {"shape": "FB", "thickness": 19, "width": 75, "height": None, "length": None},
]

# 数値抽出
values = re.findall(r'\d+', text)

# 切断長さに変換（例：20mm引く）
cut_lengths = [int(v) - 30 for v in values]

# 長さごとに本数集計
counted = Counter(cut_lengths)

# レコード化（長さ・本数）
records = [{"長さ": length, "本数": count} for length, count in counted.items()]

# 表示
for r in records:
    print(r)