'''
참고URL
https://github.com/sharebook-kr/pyupbit

프로젝트github 및 구동 URL
https://github.com/jjn3912/AI-coweb/tree/main
http://jjn3912.iptime.org:8080/
'''

'''
History
2024 04 04 비트코인 캔들차트 1분, 60분, 1일 생성
'''
import os
import threading
import pyupbit
import datetime
import time
import plotly.graph_objects as go
import pandas as pd

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'


def candlestick_chart(ticker, interval):
    df = pyupbit.get_ohlcv(ticker=ticker, interval=interval, count=300)
    df.index = pd.to_datetime(df.index)
    while True:
        fig = go.Figure(
            data=[
                go.Candlestick(
                    x=df.index,
                    open=df['open'],
                    high=df['high'],
                    low=df['low'],
                    close=df['close'],
                    increasing_line=dict(color="red"),
                    decreasing_line=dict(color="blue"),
                )
            ],
            layout=go.Layout(
                title=go.layout.Title(text=f'{ticker, interval}, 캔들차트')
            )
        )
        fig.show()

        cur_time = datetime.datetime.now()
        cur_min_dt = cur_time - datetime.timedelta(seconds=1)
        current_price = pyupbit.get_current_price(ticker)
        close_price = current_price

        if cur_min_dt > df.index[-1]:
            new_data = pyupbit.get_ohlcv(ticker=ticker, interval=interval, count=1)
            new_data.index = pd.to_datetime(new_data.index)
            df = pd.concat([df, new_data], axis=0)
        else:
            df.iloc[-1, df.columns.get_loc('close')] = close_price
            if close_price > df.iloc[-1]['high']:
                df.iloc[-1, df.columns.get_loc('high')] = close_price
            if close_price < df.iloc[-1]['low']:
                df.iloc[-1, df.columns.get_loc('low')] = close_price

        time.sleep(60)


def current_price():
    tickers = ["KRW-BTC", "KRW-ETH", "KRW-XRP"]
    while True:
        for ticker in tickers:
            print(f"{ticker}: {pyupbit.get_current_price(ticker)}")
        time.sleep(30)

if __name__ == "__main__":
    print("직접 실행")

    '''
    interval종류 day/minute1/minute3/minute5/minute10/minute15/minute30/minute60/minute240/week/month
    '''

    BTC_1m_thread = threading.Thread(target=candlestick_chart, args=("KRW-BTC", "minute1",))
    BTC_1m_thread.start()

    BTC_1h_thread = threading.Thread(target=candlestick_chart, args=("KRW-BTC", "minute60",))
    BTC_1h_thread.start()

    BTC_1h_thread = threading.Thread(target=candlestick_chart, args=("KRW-BTC", "day",))
    BTC_1h_thread.start()

    price_thread = threading.Thread(target=current_price)
    price_thread.start()

    # ETH_thread = threading.Thread(target=candlestick_chart, args=("KRW-ETH",))
    # ETH_thread.start()
    # ETH_thread.join()
    # XRP_thread = threading.Thread(target=candlestick_chart, args=("KRW-XRP",))
    # XRP_thread.start()
    # XRP_thread.join()