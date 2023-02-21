"""https://blog.gnkm.info/pandas-concat の記事で扱ったソースコード
"""

import pandas as pd

SEPARATOR = " ===== ===== ===== "


def print_heading(title):
    print(f"\n{SEPARATOR} {title} {SEPARATOR}")


# 元となる DataFrame `df1_1`, `df2_1` を作る。
df1_1 = pd.DataFrame({"col1": [i for i in range(5)]})
print_heading("df1_1")
print(df1_1.to_markdown())
# output
"""
 ===== ===== =====  df1_1  ===== ===== =====
|    |   col1 |
|---:|-------:|
|  0 |      0 |
|  1 |      1 |
|  2 |      2 |
|  3 |      3 |
|  4 |      4 |
"""
df2_1 = pd.DataFrame({"col2": [i for i in range(5, 10)]})
print_heading("df2_1")
print(df2_1.to_markdown())
# output
"""
 ===== ===== =====  df2_1  ===== ===== =====
|    |   col2 |
|---:|-------:|
|  0 |      5 |
|  1 |      6 |
|  2 |      7 |
|  3 |      8 |
|  4 |      9 |
"""

# `df1_1`, `df2_1` を一部切り出す。
df1_2 = df1_1.iloc[:2]
print_heading("df1_2")
print(df1_2.to_markdown())
# output
"""
 ===== ===== =====  df1_2  ===== ===== =====
|    |   col1 |
|---:|-------:|
|  0 |      0 |
|  1 |      1 |
"""

df2_2_ng = df2_1.loc[3:4]
print_heading("df2_2_ng")
print(df2_2_ng.to_markdown())
# output
"""
 ===== ===== =====  df2_2_ng  ===== ===== =====
|    |   col2 |
|---:|-------:|
|  3 |      8 |
|  4 |      9 |
"""

df3_1 = pd.concat([df1_2, df2_2_ng], axis="columns")
print_heading("df3_1")
print(df3_1.to_markdown())
# output
"""
 ===== ===== =====  df3_1  ===== ===== =====
|    |   col1 |   col2 |
|---:|-------:|-------:|
|  0 |      0 |    nan |
|  1 |      1 |    nan |
|  3 |    nan |      8 |
|  4 |    nan |      9 |
"""

# この状態で複数列を使った演算を行っても下記のようになる。
df3_1["col1_plus_col2"] = df3_1["col1"] + df3_1["col2"]
print_heading("df3_1")
print(df3_1.to_markdown())
# output
"""
 ===== ===== =====  df3_1  ===== ===== =====
|    |   col1 |   col2 |   col1_plus_col2 |
|---:|-------:|-------:|-----------------:|
|  0 |      0 |    nan |              nan |
|  1 |      1 |    nan |              nan |
|  3 |    nan |      8 |              nan |
|  4 |    nan |      9 |              nan |
"""

# 意図した DataFrame を作るためには `reset_index()` を行う必要がある。
df2_2_ok = df2_1.loc[3:4].reset_index(drop=True)
print_heading("df2_2_ok")
print(df2_2_ok.to_markdown())
# output
"""
 ===== ===== =====  df2_2_ok  ===== ===== =====
|    |   col2 |
|---:|-------:|
|  0 |      8 |
|  1 |      9 |
"""

df4_1 = pd.concat([df1_2, df2_2_ok], axis="columns")
print_heading("df4_1")
print(df4_1.to_markdown())
# output
"""
 ===== ===== =====  df4_1  ===== ===== =====
|    |   col1 |   col2 |
|---:|-------:|-------:|
|  0 |      0 |      8 |
|  1 |      1 |      9 |
"""

df4_1["col1_plus_col2"] = df4_1["col1"] + df4_1["col2"]
print_heading("df4_1")
print(df4_1.to_markdown())
# output
"""
 ===== ===== =====  df4_1  ===== ===== =====
|    |   col1 |   col2 |   col1_plus_col2 |
|---:|-------:|-------:|-----------------:|
|  0 |      0 |      8 |                8 |
|  1 |      1 |      9 |               10 |
"""
