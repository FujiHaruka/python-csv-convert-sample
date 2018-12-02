# Python で CSV ファイルのデータ処理

This repository is in personal use.

## Anaconda をインストールして Python 実行環境を準備する

[Anaconda](https://www.anaconda.com/) は Python 実行環境とパッケージ管理をまとめて簡単に行ってくれる。しかもインストールが簡単。

簡単にインストールするなら Anaconda Navigator をインストールすればいい。Mac のアプリになっていて、インストールするだけで Python の環境準備が完了する。Mac でのインストール方法は https://qiita.com/ShibaNDD/items/61624a947651caee40a0 を参照（現在は Python 3.7 がインストールされる）。

インストールができたらターミナルを開き、Python のバージョンを確認する。

```
$ python -V
Python 3.7.0
```

バージョンが `3.7.x` なら Anaconda の Python が使われている。（バージョンが `2.7.x` なら Mac のデフォルトの Python が使われているため、Anaconda の Python ではない。）

## convert.py を実行する

まずこのリポジトリをダウンロードする。（右上に Clone or download ボタンがありますよね？）

ターミナルを開き、このリポジトリに移動する。

```sh
# ディレクトリを移動する
$ cd path/to/python-csv-convert
```

`convert.py` を実行してみる。

```
# python [スクリプトファイル名] で python スクリプトを実行する
$ python convert.py
```

すると、`output.csv` ファイルが作成される。

`convert.py` スクリプトがやっていることは、 `samples/original.csv` ファイルを読み込んで、データ処理を行い、`output.csv` を出力する。

`output.csv` の中身を確認すると、データ処理後の CSV ファイルになっているはず。

```sh
$ open output.csv
```

