# IMDb Top 100 Movies Scraper

IMDbのトップ100映画リストを自動的にスクレイピングし、データを収集・分析するプロジェクトです。

## 機能

- IMDbのトップ100映画リストの自動スクレイピング
- 映画のタイトル、公開年、評価、URLの取得
- データのCSVファイルへの保存
- 評価分布の可視化
- 毎日午前9時に自動実行

## 必要条件

- **Python 3.x**（3.8以上推奨）
- **Google Chrome**（最新バージョン）
- **ChromeDriver**（`webdriver_manager` で自動管理）
- **仮想環境（venv）**

## 📥 インストール & セットアップ

### **1️⃣ リポジトリをクローン**
```sh
git clone https://github.com/yourusername/imdb-top100-scraper.git
cd imdb-top100-scraper
```
## 📥 インストール & セットアップ

### **1️⃣ リポジトリをクローン**

1. リポジトリをクローン
2. 仮想環境を作成
3. 依存パッケージをインストール
4. スクレイピングを実行
5. データをCSVファイルに保存
6. 評価分布を可視化
7. 毎日午前9時に自動実行

# 仮想環境を作成
python3 -m venv venv
source venv/bin/activate
venv/Scripts/activate

# 依存パッケージをインストール
pip install -r requirements.txt

# 実行方法(スクレイピングを手動実行する場合)
python3 scraper.py

# 実行方法(スケジューラーを実行する場合)
python3 scheduler.py
