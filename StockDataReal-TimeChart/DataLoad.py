import requests
from bs4 import BeautifulSoup
import openpyxl



fpath = r'C:\Users\rch\Desktop\대학관련\github\StockDataReal-TimeChart\StockData.xlsx'
wb = openpyxl.load_workbook(fpath)
ws = wb.active # 현재 활성화된 시트 선택


add_code = int(input("종목 추가: "))


# 종목 리스트
codes = [
    '036570', # NC
    '005930', # 삼성전자
    '373220'  # LG 에너지 솔루션
]

for i in range(add_code):
    code = input("종목 코드 입력: ")
    codes.append(code)

row = 2 # row값 2부터 시작해서. row 1은 변수명

for code in codes:
    url = f"https://finance.naver.com/item/sise.naver?code={code}"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.select_one("#_nowVal").text

    price = price.replace(',', '')

    print(price)
    
    ws[f'B{row}'] = int(price) #위에 row값에 숫자. 확인
    row = row + 1
wb.save(fpath)