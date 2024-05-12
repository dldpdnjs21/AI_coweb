'''
코인학습에 필요한 xml, json, csv파일 수집

1. 석유 ㅇ
2. 금 ㅇ
3. 달러 ㅇ
4. 나스닥 ㅇ
5. 반감기 X (데이터존재X)
   비트코인을 채굴할 수 있는 양을 반토막냄(가치를 높임)
6. 수요와 공급(데이터)
7. 채굴난이도 X (데이터존재X)

각 Colum과 각 코인차트들의 시가,종가...를 매치해야할것같다.
따라서 github에 각코인의 수만큼 csv가 필요할것같다.

데이터 수집URL
https://www.opec.org/opec_web/en/data_graphs/40.htm opec -석유수수출기구
https://kr.investing.com/currencies/usd-krw-historical-data - 인베스팅닷컴
'''


import os
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import pyupbit
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

#df = pd.read_csv('https://raw.githubusercontent.com/jjn3912/AI-coweb/main/src/csv/Coin.csv?token=GHSAT0AAAAAACQIYMABPLUQDZ2H5X3WELJIZQT43EQ' ,encoding='cp949')
#df = pd.read_csv('C:/Coin.csv', encoding='cp949')
#print(df.shape)
'''
문제점
https://wikidocs.net/173005 를 참고하여
RNN 신경망으로 하루를 예측해보려했는데 한달데이터로 하루를 예측하는게 가능한것인가 라는생각이듬
n달전데이터로 그다음달 에측-> 다음달 시가 예측 -> 코인인데 의미없다 판단
또 shape호출결과 df데이터가 부족할것이라고 판단
한달주기데이터X, 일일주기데이터로 변환 필요
2024 04 11 (목)
프로젝트팀에게 csv를 일별로 변환한다고 상의 후
Coin.csv를 일별로 변환후 다시 merge진행
'''

# colum의 형태에 맞춰 split(), merge(), concat()
# splited = oil_df['Date'].str.split(' ', expand=True)
# print(splited)
# splited.columns=['Date', 'oil Price']
# print(splited)
# splited.to_csv('oil_df.csv')
# btc_df = pyupbit.get_ohlcv(ticker="KRW-BTC", interval="day1", to='20240402', count=2283)
# Date_df = pd.read_csv('C:/Date.csv', encoding='cp949')
# oil_df = pd.read_csv('C:/oil_df.csv', encoding='cp949')
# usd_df = pd.read_csv('C:/Usd.csv', encoding='cp949')
# Kospi_df = pd.read_csv('C:/Kospi.csv', encoding='cp949')
# Gold_df = pd.read_csv('C:/Gold.csv', encoding='cp949')
# splited = oil_df['Date'].str.split(' ', expand=True)
# print(splited)
# splited.columns=['Date', 'oil Price']
# print(splited)
# splited.to_csv('oil_df2.csv')
# df = pd.merge(Date_df, oil_df, on='Date', how='outer')
# df = pd.merge(df, usd_df, on='Date', how='outer')
# df = pd.merge(df, Kospi_df, on='Date', how='outer')
# df = pd.merge(df, Gold_df, on='Date', how='outer')
# df = pd.concat([df, btc_df], axis=1)
# df.to_csv('result.csv')

#read_df = pd.read_csv('https://raw.githubusercontent.com/jjn3912/AI-coweb/main/src/csv/result.csv', encoding='cp949')

# read_df = pd.read_csv('c:/result.csv', encoding='cp949')
# df = read_df.dropna()
# # print(df.columns)
# # print(df.shape)
# dates = pd.to_datetime(df["Date"])
# X = list(df)[1:11]
# df = df[X].astype(float)

# def MinMaxScaler(data):
#     numerator = data - np.min(data, 0)
#     denominator = np.max(data, 0) - np.min(data, 0)
#     return numerator / (denominator + 1e-7)
#
#
# dfx = df[['oil Price', 'Usd', 'Kospi', 'gold', 'open', 'high', 'low', 'volume', 'value', 'close']]
# dfx = MinMaxScaler(dfx)
# dfy = dfx['close']
# dfx = df[['oil Price', 'Usd', 'Kospi', 'gold', 'open', 'high', 'low', 'volume', 'value']]
#
# # 두 데이터를 리스트 형태로 저장
# X = dfx.values.tolist()
# y = dfy.values.tolist()
#
# window_size = 10
#
# data_X = []
# data_y = []
# for i in range(len(y) - window_size):
#     _X = X[i : i + window_size] # 다음 날 종가(i+windows_size)는 포함되지 않음
#     _y = y[i + window_size]     # 다음 날 종가
#     data_X.append(_X)
#     data_y.append(_y)
#
# train_size = int(len(data_y) * 0.7)
# train_X = np.array(data_X[0 : train_size])
# train_y = np.array(data_y[0 : train_size])
#
# test_size = len(data_y) - train_size
# test_X = np.array(data_X[train_size : len(data_X)])
# test_y = np.array(data_y[train_size : len(data_y)])
#
# print('훈련 데이터의 크기 :', train_X.shape, train_y.shape)
# print('테스트 데이터의 크기 :', test_X.shape, test_y.shape)
#
# model = Sequential()
# model.add(LSTM(units=20, activation='relu', return_sequences=True, input_shape=(10, 9)))
# model.add(Dropout(0.1))
# model.add(LSTM(units=20, activation='relu'))
# model.add(Dropout(0.1))
# model.add(Dense(units=1))
# model.summary()
#
# model.compile(optimizer='adam', loss='mean_squared_error')
# model.fit(train_X, train_y, epochs=50, batch_size=30)
# pred_y = model.predict(test_X)  # test_X에 대한 예측값을 구합니다.
#
# plt.figure()
# plt.plot(dates[train_size:], test_y, color='red', label='real SEC stock price')
# plt.plot(dates[train_size:], pred_y, color='blue', label='predicted SEC stock price')
# plt.title('SEC stock price prediction')
# plt.xlabel('time')
# plt.ylabel('stock price')
# plt.legend()
# plt.show()
'''
2024 04 12 딥러닝 진행
https://chat.openai.com/c/47c7040c-570f-47e4-9ca0-406b99c5d51b을 참고하여
ValueError: x and y must have same first dimension, but have shapes (314,) and (304,) 해결하기
2024 04 15 코인의 하루데이터도 의미없다고 판단, 원활한 데이터처리와 캔들차트삽입을 위해 분당데이터로만 처리
'''

# df = pyupbit.get_ohlcv(ticker="KRW-BTC", interval = "minute1", to="20240430", count=2000000)
# print(df)
# df.to_pickle('btc min per price.pickle')
# df.to_csv('btc min per price.csv')

# import gzip
#
#
# df2 = pd.read_pickle('btc min per price.pickle') #불러오기
# print(df2)
# with gzip.open('btc min per price.pickle.gz', 'wb') as f:
#      f.write(df2.encode('utf-8'))

import pandas as pd
import gzip

# 피클 파일에서 DataFrame 불러오기
df2 = pd.read_pickle('btc min per price.pickle')

# DataFrame을 gzip을 사용하여 압축하여 저장하기
with gzip.open('btc min per price.pickle.gz', 'wb') as f:
     df2.to_pickle(f)

