"""https://blog.gnkm.info/pandas-concat の記事で扱ったソースコード
"""
import pandas as pd

SEPARATOR = " ===== ===== ===== "


def print_heading(title=''):
    print(f"\n{SEPARATOR} {title} {SEPARATOR}")


# 元となる DataFrame `df1`, `df2` を作る。
df1 = pd.DataFrame({"col1": [i for i in range(5)]})
print_heading("df1")
print(df1.to_markdown())
# output
"""
 ===== ===== =====  df1  ===== ===== =====
|    |   col1 |
|---:|-------:|
|  0 |      0 |
|  1 |      1 |
|  2 |      2 |
|  3 |      3 |
|  4 |      4 |
"""
df2 = pd.DataFrame({"col2": [i for i in range(5, 10)]})
print_heading("df2")
print(df2.to_markdown())
# output
"""
 ===== ===== =====  df2  ===== ===== =====
|    |   col2 |
|---:|-------:|
|  0 |      5 |
|  1 |      6 |
|  2 |      7 |
|  3 |      8 |
|  4 |      9 |
"""

# `df1`, `df2` を一部切り出す。
df1_sliced = df1.iloc[:2]
print_heading("df1_sliced")
print(df1_sliced.to_markdown())
# output
"""
 ===== ===== =====  df1_sliced  ===== ===== =====
|    |   col1 |
|---:|-------:|
|  0 |      0 |
|  1 |      1 |
"""

df2_sliced_simply = df2.loc[3:4]
print_heading("df2_sliced_simply")
print(df2_sliced_simply.to_markdown())
# output
"""
 ===== ===== =====  df2_sliced_simply  ===== ===== =====
|    |   col2 |
|---:|-------:|
|  3 |      8 |
|  4 |      9 |
"""

df3_ng = pd.concat([df1_sliced, df2_sliced_simply], axis="columns")
print_heading("df3_ng")
print(df3_ng.to_markdown())
# output
"""
 ===== ===== =====  df3_ng  ===== ===== =====
|    |   col1 |   col2 |
|---:|-------:|-------:|
|  0 |      0 |    nan |
|  1 |      1 |    nan |
|  3 |    nan |      8 |
|  4 |    nan |      9 |
"""

# この状態で複数列を使った演算を行っても下記のようになる。
df3_ng["col1_plus_col2"] = df3_ng["col1"] + df3_ng["col2"]
print_heading("df3_ng")
print(df3_ng.to_markdown())
# output
"""
 ===== ===== =====  df3_ng  ===== ===== =====
|    |   col1 |   col2 |   col1_plus_col2 |
|---:|-------:|-------:|-----------------:|
|  0 |      0 |    nan |              nan |
|  1 |      1 |    nan |              nan |
|  3 |    nan |      8 |              nan |
|  4 |    nan |      9 |              nan |
"""

# 意図した DataFrame を作るためには `reset_index()` を行う必要がある。
df2_sliced_reset_index = df2.loc[3:4].reset_index(drop=True)
print_heading("df2_sliced_reset_index")
print(df2_sliced_reset_index.to_markdown())
# output
"""
 ===== ===== =====  df2_sliced_reset_index  ===== ===== =====
|    |   col2 |
|---:|-------:|
|  0 |      8 |
|  1 |      9 |
"""

df3_ok = pd.concat([df1_sliced, df2_sliced_reset_index], axis="columns")
print_heading("df3_ok")
print(df3_ok.to_markdown())
# output
"""
 ===== ===== =====  df3_ok  ===== ===== =====
|    |   col1 |   col2 |
|---:|-------:|-------:|
|  0 |      0 |      8 |
|  1 |      1 |      9 |
"""

df3_ok["col1_plus_col2"] = df3_ok["col1"] + df3_ok["col2"]
print_heading("df3_ok")
print(df3_ok.to_markdown())
# output
"""
 ===== ===== =====  df3_ok  ===== ===== =====
|    |   col1 |   col2 |   col1_plus_col2 |
|---:|-------:|-------:|-----------------:|
|  0 |      0 |      8 |                8 |
|  1 |      1 |      9 |               10 |
"""
