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
<br>

1단계:
<br>-12/20: 주식 투자 자동화 파이썬 코드 분석. yaml파일 오류 확인. 수정 예정
<br>-12/21: 모의 투자로 변경(config.yaml)
<br>-12/22: config.yaml파일 로드,colab환경 정상 작동, vscode환경 오류. 수정 예정
<br>-12/23: config.yaml파일 로드, vscode환경 오류 문제 해결. 1단계 종료.
<br>
<br>
2단계
<br> -12/28: 종목 현재가 불러와서 excel파일에 실시간 반영.
