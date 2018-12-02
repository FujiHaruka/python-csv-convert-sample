# Python で行う CSV ファイルのデータ処理

This repository is in personal use.

## Anaconda で Python 実行環境を準備する

[Anaconda](https://www.anaconda.com/) は Python 実行環境とパッケージ管理をまとめて簡単に行ってくれる。インストールが簡単なので初心者向け。

一番楽なのは Anaconda Navigator をインストールすればいい。Mac のアプリになっていて、インストールするだけで Python の環境準備が完了する。Mac でのインストール方法は https://qiita.com/ShibaNDD/items/61624a947651caee40a0 を参照（現在は Python 3.7 がインストールされる）。

インストールができたらターミナルを開き、Python のバージョンを確認する。

```
$ python -V
Python 3.7.0
```

バージョンが `3.7.x` なら Anaconda の Python が使われているのでインストール成功。（バージョンが `2.7.x` なら Mac のデフォルトの Python が使われているため、Anaconda の Python ではない。）

## データ処理の Python スクリプトを実行する

目標はこのリポジトリにある `convert.py` を実行すること。

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

## ライブラリの解説

`convert.py` の中で pandas を使っている。pandas は表計算を支援するライブラリで、CSV ファイルをいろいろデータ処理するならこれ。

ドキュメントは https://pandas.pydata.org/pandas-docs/stable/index.html

pandas の入門記事はググるといろいろ出てくる。とりあえず DataFrame クラスと Series クラスが理解できれば使えるようになる。
