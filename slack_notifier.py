import requests
import json
import os

def send_slack_notification(message):
    url = os.getenv("SLACK_WEBHOOK_URL") # 環境変数からURLを取得

    if not url:
        print("Slack Webhook URLが設定されていません。")
        return

    payload = {"text": message}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, data=json.dumps(payload), headers=headers)

    if response.status_code == 200:
        print("Slack通知が送信されました")
    else:
        print(f"Slack通知の送信に失敗しました: {response.status_code}")

# テスト
send_slack_notification("テスト通知です")