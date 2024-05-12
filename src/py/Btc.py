import os
import threading
import pyupbit
import datetime
import time
import plotly.graph_objects as go
import pandas as pd

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'


def btc_min():
    btc_df_min = pyupbit.get_ohlcv(ticker="KRW-BTC", inter="minute1", count=100)
    btc_df_min.index = pd.to_datetime(btc_df_min.index)  # 인덱스를 datetime 형식으로 변환
    while True:
        btc_df_min.index = pd.to_datetime(btc_df_min.index)  # 인덱스를 datetime 형식으로 변환
        # 현재 시간
        cur_time = datetime.datetime.now()
        # 현재 시간의 바로 이전 분의 데이터 가져오기
        cur_min_dt = cur_time - datetime.timedelta(minutes=1)
        # 현재 가격 데이터 가져오기
        current_price = pyupbit.get_current_price("KRW-BTC")
        close_price = current_price

        # 새로운 분의 데이터인지 확인하고 업데이트
        if cur_min_dt > btc_df_min.index[-1]:
            new_data = pyupbit.get_ohlcv(ticker="KRW-BTC", inter="minute1", count=1)
            new_data.index = pd.to_datetime(new_data.index)  # 새로운 데이터의 인덱스를 datetime 형식으로 변환
            # 새로운 데이터를 btc_df_min에 추가하기
            btc_df_min = pd.concat([btc_df_min, new_data], axis=0)

        else:
            # 이미 있는 분의 데이터면 가격 정보만 업데이트
            btc_df_min.iloc[-1, btc_df_min.columns.get_loc('close')] = close_price
            if close_price > btc_df_min.iloc[-1]['high']:
                btc_df_min.iloc[-1, btc_df_min.columns.get_loc('high')] = close_price
            if close_price < btc_df_min.iloc[-1]['low']:
                btc_df_min.iloc[-1, btc_df_min.columns.get_loc('low')] = close_price
        fig = go.Figure(
            data=[
                go.Candlestick(
                    x=btc_df_min.index,
                    open=btc_df_min['open'],
                    high=btc_df_min['high'],
                    low=btc_df_min['low'],
                    close=btc_df_min['close'],
                    increasing_line=dict(color="red"),  # 상승 시 빨간색으로 설정
                    decreasing_line=dict(color="blue"),  # 하락 시 파란색으로 설정
                )
            ],
            layout=go.Layout(
                title=go.layout.Title(text='KRW-BTC, 캔들차트')
            )
        )
        fig.show()
        # 1분마다 업데이트
        time.sleep(60)


if __name__ == "__main__":
    print("직접 실행")
    print(__name__)
else:
    print("main에서 임포트되어 사용됨")
    print(__name__)


#0.5초마다 최근 체결가격 조회
def current_price():
    tickers = ["KRW-BTC", "KRW-ETH", "KRW-XRP"]  # 티커 리스트
    while True:
        for ticker in tickers:
            print(f"{ticker}: {pyupbit.get_current_price(ticker)}")
        time.sleep(0.5)


thread1 = threading.Thread(target=btc_min)
thread2 = threading.Thread(target=current_price)

# 스레드 시작
thread1.start()
thread2.start()

# 메인 스레드가 종료되기 전에 스레드가 모두 종료되도록 대기
thread1.join()
thread2.join()
