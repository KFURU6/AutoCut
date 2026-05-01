import re
from collections import Counter

text = "A=1000 B=500 C=1000 D=500 E=250"

# 各鋼材のリスト
# L5×50,
# □-5×50×50,
# C-5×50×50,
# FB-3×32,

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