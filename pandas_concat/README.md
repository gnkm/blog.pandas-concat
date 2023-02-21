# DataFrame の複数列を使う演算を行うためには index が揃っている必要がある

https://blog.gnkm.info/pandas-concat の記事で扱ったソースコード。

## Usage

### Create virtual env

```
anyenv install pyenv
pyenv install 3.8.13
poetry env use $HOME/.anyenv/envs/pyenv/versions/3.8.13/bin/python
```

### Prepare

```
poetry shell
poetry install
```

### Execute

```
python pandas_concat.py
```

### Exit virtual env

```
exit
```
