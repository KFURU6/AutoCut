import re
from collections import Counter

text = "A=1000 B=500 C=1000 D=500 E=250"

# 各鋼材のリスト
data = [
    # L形鋼
    {"shape": "L", "thickness": 3, "width": 30, "depth": None},
    {"shape": "L", "thickness": 3, "width": 40, "depth": None},
    {"shape": "L", "thickness": 4, "width": 50, "depth": None},
    {"shape": "L", "thickness": 6, "width": 50, "depth": None},
    {"shape": "L", "thickness": 6, "width": 65, "depth": None},
    {"shape": "L", "thickness": 6, "width": 75, "depth": None},

    # 角パイプ（□）
    {"shape": "□", "thickness": 1.6, "width": 25, "depth": None},
    {"shape": "□", "thickness": 1.6, "width": 31, "depth": None},
    {"shape": "□", "thickness": 1.6, "width": 40, "depth": None},
    {"shape": "□", "thickness": 2.3, "width": 50, "depth": None},
    {"shape": "□", "thickness": 2.3, "width": 45, "depth": 75},
    {"shape": "□", "thickness": 2.3, "width": 50, "depth": 100},
    {"shape": "□", "thickness": 3.2, "width": 75, "depth": 125},

    # チャンネル（C）
    {"shape": "C", "thickness": 5, "width": 40, "depth": 75},
    {"shape": "C", "thickness": 5, "width": 50, "depth": 100},
    {"shape": "C", "thickness": 6, "width": 65, "depth": 125},
    {"shape": "C", "thickness": 6.5, "width": 75, "depth": 150},
    {"shape": "C", "thickness": 8, "width": 90, "depth": 200},

    # フラットバー（FB）
    {"shape": "FB", "thickness": 3, "width": 32, "depth": None},
    {"shape": "FB", "thickness": 4.5, "width": 44, "depth": None},
    {"shape": "FB", "thickness": 6, "width": 90, "depth": None},
    {"shape": "FB", "thickness": 9, "width": 100, "depth": None},
    {"shape": "FB", "thickness": 19, "width": 75, "depth": None},
]

# 数値抽出
values = re.findall(r'\d+', text)

# 切断長さに変換（例：20mm引く）
cut_lengths = [int(v) - 20 for v in values]

# 長さごとに本数集計
counted = Counter(cut_lengths)

# レコード化（長さ・本数）
records = [{"長さ": length, "本数": count} for length, count in counted.items()]

# 表示
for r in records:
    print(r)