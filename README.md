# IMDb Top 100 Movies Scraper

IMDbのトップ100映画リストを自動的にスクレイピングし、データを収集・分析するプロジェクトです。

## 🎯 機能

- IMDbのトップ100映画リストの自動スクレイピング
- 映画のタイトル、公開年、評価、URLの取得
- データのCSVファイルへの保存
- 評価分布の可視化
- 毎日午前9時に自動実行

## 🔧 必要条件

- Python 3.x（3.8以上推奨）
- Google Chrome（最新バージョン）
- ChromeDriver（`webdriver_manager` で自動管理）
- 仮想環境（venv）

## 📥 インストール & セットアップ

### 1. リポジトリをクローン
```bash
git clone https://github.com/yourusername/imdb-top100-scraper.git
cd imdb-top100-scraper
```

### 2. 仮想環境のセットアップ
```bash
# 仮想環境を作成
python3 -m venv venv

# 仮想環境を有効化
# Mac / Linux の場合
source venv/bin/activate
# Windowsの場合
venv\Scripts\activate
```

### 3. パッケージのインストール
```bash
pip install -r requirements.txt
```

## 🚀 実行方法

### 手動実行
```bash
python3 scraper.py
```
実行後、`imdb_top100_movies_selenium.csv` にデータが保存されます。

### 自動実行
```bash
python3 scheduler.py
```
- 毎日午前9時にscraper.pyを自動実行します
- テスト用: `scheduler.py` 内の時間設定を `schedule.every(1).minute.do(job)` に変更できます

## 📊 データの可視化
```bash
python3 scraper.py
```