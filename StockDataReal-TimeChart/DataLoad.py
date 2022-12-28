import requests
from bs4 import BeautifulSoup


# 종목 리스트
codes = [
    '036570', # NC
    '005930', # 삼성전자
    '373220'  # LG 에너지 솔루션
]


for code in codes:
    url = f"https://finance.naver.com/item/sise.naver?code={code}"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.select_one("#_nowVal").text

    price = price.replace(',', '')

    print(price)