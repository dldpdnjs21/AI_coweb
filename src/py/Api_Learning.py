'''
코인학습에 필요한 xml, json, csv파일 수집

1. 석유
2. 금
3. 달러
4. 반감기
   비트코인을 채굴할 수 있는 양을 반토막냄(가치를 높임)
5. 수요와 공급(데이터)
6. 채굴난이도

데이터 수집URL
https://www.opec.org/opec_web/en/data_graphs/40.htm opec -석유수수출기구
http://data.krx.co.kr/ -정보데이터시스템
'''
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/jjn3912/AI-coweb/main/src/csv/Coin.csv?token=GHSAT0AAAAAACQIYMABGTMRYKD5RKYDHQWIZQSQHLA' ,encoding='cp949')
#df = pd.read_csv('C:/Coin.csv' ,encoding='cp949')
dates = pd.to_datetime(df["Date"])
print(df)




