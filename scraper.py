from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
import pandas as pd
import matplotlib.pyplot as plt

chrome_options = Options()
chrome_options.add_argument("--headless=new")  # 新しいheadlessモードを使用
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--window-size=1920,1080")  # 明示的にウィンドザサイズを設定
chrome_options.add_argument("--disable-gpu")  # GPUの使用を無効化
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")  # User-Agentを設定

# リトライ用関数
def retry_driver_get(driver, url, retries=3, delay=5):
    for attempt in range(retries):
        try:
            driver.get(url)
            return True
        except TimeoutException:
            print(f"Timeout occurred, retrying {attempt + 1}/{retries}...")
            logging.error(f"Timeout occurred, retrying {attempt + 1}/{retries}...")
            time.sleep(delay)
    return False

def scrape_imdb_top_100():
    # WebDriverのセットアップ
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # ページの読み込みを待つ時間を増やす
    driver.implicitly_wait(20)

    # IMDbのトップ100にアクセス
    target_url = "https://www.imdb.com/chart/top"
    driver.get(target_url)

    # より長い待機時間を設定
    wait = WebDriverWait(driver, 20)

    # 要素が見つかるまで待機
    movie_rows = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "sc-d5ea4b9d-0")))

    # 取得情報を格納するリスト
    movies = []

    # 映画タイトル、公開年、URLを取得
    for movie in movie_rows:
        try:
            movie_title = movie.find_element(By.TAG_NAME, "a").text
            year = movie.find_element(By.CSS_SELECTOR, "div.sc-d5ea4b9d-6.hBxwRe.cli-title-metadata > span:nth-child(1)").text
            review = movie.find_element(By.CLASS_NAME, "ipc-rating-star--rating").text
            movie_url = movie.find_element(By.TAG_NAME, "a").get_attribute("href")
            # 映画データをリストに追加
            movies.append([movie_title, year, review, movie_url])
        except Exception as e:
            print(f"エラーが発生しました: {e}")

    # 取得したデータを表示
    for movie in movies:
        print(movie)

    # DataFrameに変換してCSVに保存
    df = pd.DataFrame(movies, columns=["映画タイトル", "公開年", "評価", "URL"])
    df.to_csv("imdb_top_100_movies_selenium.csv", index=False, encoding="utf-8-sig")

    # 評価を抽出（修正）
    ratings = df['評価'].astype(float).tolist()

    # 評価分布をヒストグラムで表示
    plt.figure(figsize=(10, 6))
    plt.hist(ratings, bins=20, edgecolor='black')
    plt.title('映画評価の分布')
    plt.xlabel('評価')
    plt.ylabel('映画数')
    plt.show()

    # 公開年ごとの評価
    df["公開年"] = pd.to_datetime(df["公開年"], errors="coerce").dt.year
    year_rating_count = df.groupby(["公開年", "評価"]).size().unstack().fillna(0)

    # 公開年ごとの評価分布をプロット
    year_rating_count.plot(kind="bar", figsize=(12, 6), stacked=True)
    plt.title("公開年ごとの評価分布")
    plt.xlabel("公開年")
    plt.ylabel("映画数")
    plt.legend(title="評価")
    plt.xticks(rotation=90)
    plt.show()

    # ブラウザを閉じる
    driver.quit()

if __name__ == "__main__":
    scrape_imdb_top_100()
