#import requests
#from bs4 import BeautifulSoup


#url = "https://finance.naver.com/item/sise_day.naver?code=005930&page=1"


#headers = {
#    'user-agent': 'Mozilla/5.0' ##### user-agent 값 가져온 것.
#}

#resp = requests.get(url, headers = headers)

#soup = BeautifulSoup(resp.text, 'html5lib')
#css_selector = "body > table.type2 > tbody > tr > td:nth-child(2) > span" ## html 행 나타내는 tr로 가져오기. (날짜별 종가)
#result = soup.select(css_selector)

#close  = []


#for item in result:
#   close.append(item.text)

#print(close)

import requests
import json
from pandas import DataFrame

url = "https://api.finance.naver.com/siseJson.naver?symbol=005930&requestType=1&startTime=20220407&endTime=20221231&timeframe=day"
result = requests.post(url)

data = result.text.replace("'", '"').strip()
data =  json.loads(data)
print(type(data))

df = DataFrame(data[1:], columns = data[0])
df = df.set_index('날짜')
print(df.head())

#print(type(result.text))