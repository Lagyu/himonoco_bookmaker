# himonoco_bookmaker
ひものこ用ブックメーカーです。<br>
Djangoで書かれています。

## 使い方（Windowsの場合）
1. pythonをインストール
```
choco install python
```
1. ファイルの場所に移動する
```
cd path\to\himonoco_bookmaker
```
1. 仮想環境を作ってアクティベート
```
python -m venv venv
venv\Scripts\activate
```
1. パッケージのインストール
```
cd himonoco
pip install requirements.txt
```
1. DBの設定
  - settings.pyのDATABASESを適当に書き換える
  - 一部機能はSQLiteでは機能しないので気をつけてください
1. サーバを起動
```
python manage.py runserver
```
