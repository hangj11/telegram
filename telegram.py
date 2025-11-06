import requests
import json
import random
from bs4 import BeautifulSoup

bot_token = ""

chat_id = ""

def send_message(message):
    # message = input("message: ")
    data = {"chat_id": chat_id, "text": message}

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    res = requests.get(url, data=data)

    if res.status_code == 200:
        return json.loads(res.text)

keyword = random.choice(["인공지능", "AI", "챗GPT", "openai", "손흥민"])

url = f"https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query={keyword}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9"
    }

res = requests.get(url, headers=headers)

title_list = []

if res.status_code == 200:
    html = res.text

    soup = BeautifulSoup(html, "html.parser")

    titles = soup.select(".title_link")

    for title in titles:
        # print(title.text)
        title_list.append(f"{title.text}\n{title['href']}")

    print(title_list)

    message = "\n".join(title_list)

    result = send_message(message)
    print(message)
