## securities_data_analysis<br>증권데이터 분석

<h5>1단계: 주식 투자 자동화</h5>
File: KoreaStockAutoTrade.py, UsaStockAutoTrade.py, config.yaml
<br>
<h7>국내 주식 투자(KoreaStockAutoTrade.py)와 미국 주식 투자(UsaStockAutoTrade.py)로 구분.<br>
KIS developers 서비스, APP_KEY, APP_SECRET(config.yaml) 값 설정하여, 본인 계좌 사용.<br>
09:00 ~ 09:05까지 전날 남은 수량 존재하면 매도. 09:05 ~ 15:15까지 매수(상승값 0.5일때). 15:15 ~ 15:20에 일괄 매도 설정. 15:20부터 프로그램 종료(주말 포함).<br>
이 모든 과정은 본인 디스코드 메시지로 전송(config.yaml)<br>

</h7>
<br>
<h5>2단계: 주식 데이터 실시간 차트 </h5>
File: DataLoad.py, StockData.xlsx
<br>원하는 주식 종목 현재가, 실시간으로 불러와서 그래프 띄우기
<br>
<br>
<h5>3단계: 데이터베이스 구축</h5>
File: DB_connect
<br> 웹 크롤링시, 속도 문제, 데이터베이스로 보완.
<br>
<br>
<h5>4단계: 웹으로 본인 계좌 잔고 확인</h5>
File: StockServer
<br> Django 활용 본인 계좌 잔고 확인 위한 웹 페이지 구축.
<br>
<br>
<h5>1단계:</h5>
-12/20: 주식 투자 자동화 파이썬 코드 분석. yaml파일 오류 확인. 수정 예정
<br>-12/21: 모의 투자로 변경(config.yaml)
<br>-12/22: config.yaml파일 로드,colab환경 정상 작동, vscode환경 오류. 수정 예정
<br>-12/23: config.yaml파일 로드, vscode환경 오류 문제 해결. 1단계 종료.
<br>
<br>
<h5>2단계</h5>
 -12/28: 종목 현재가 불러와서 excel파일에 실시간 반영.
<br> -12/30: 추가할 종목 불러와서, 현재가 excel파일에 추가.
<br> -12/31: 삼성전자 데이터(005930) 차트 DataFrame형태로 변경 후, excel파일에  저장.
<br>
<br>
<h5>3단계</h5>
 -2023/1/4: 데이터베이스 구축 시작.
<br>-1/5: DB로부터 받아온 일일 시세 데이터 조회(MarketDB.py)
<br>-1/6: Analyzer.py파일 추가
<br>
<br>
<h5>4단계</h5>
-1/12: Django활용 웹 서버 구축 시작. (StockServer 파일)
<br>-1/13: Hello폴더 추가. 본인 계좌 잔고 확인 위한 웹 페이지 구축, 진행 중 (hello 파일)
