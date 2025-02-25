import schedule
import time
import subprocess
import logging
import csv
from datetime import datetime
import sys

# ログの設定
logging.basicConfig(
    filename="scheduler.log", # ログファイル名
    level=logging.INFO, # ログレベル
    format="%(asctime)s - %(levelname)s - %(message)s" # フォーマット（時間、レベル、メッセージ）
)

def job():
    try:
        logging.info("スクレイピングを実行中")
        print("スクレイピングを実行中")
        # scraper.pyを実行
        subprocess.run([sys.executable, "scraper.py"])
        logging.info("スクレイピングが完了しました。")
    except Exception as e:
        logging.error(f"エラーが発生しました: {e}")

# 毎日午前9時にスクレイピングを実行する
schedule.every().day.at("09:00").do(job)
# schedule.every(1).minute.do(job)

# 定期的にジョブを実行
try:
    while True:
        schedule.run_pending()
        time.sleep(1)

except KeyboardInterrupt:
    # Ctrl+Cで中断された際の処理
    print("スケジューラーが終了しました。")
    logging.info("スケジューラーが手動で終了されました。")