

import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Conv1D, Lambda
from tensorflow.keras.losses import Huber
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
import os
import datetime
import numpy as np
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'


# Github에서 분할된 DataFrame 불러오기 (1,000,000개씩)
df1 = pd.read_csv("https://raw.githubusercontent.com/jjn3912/AI-coweb/main/src/py/Btcprice2.csv")
df2 = pd.read_csv("https://raw.githubusercontent.com/jjn3912/AI-coweb/main/src/py/Btcprice1.csv")
# 분할된 DataFrame 연결하기(약2,000,000개 / 2020 07 16 18:28 ~ 2024 05 10 08:59 (1분당 BTC가격 데이터)
df = pd.concat([df1, df2])

# 스케일을 적용할 column을 정의합니다.
scaler = MinMaxScaler()
scale_cols = ['open', 'high', 'low', 'close', 'volume', 'value']
# 스케일 후 columns
scaled = scaler.fit_transform(df[scale_cols])
df = pd.DataFrame(scaled, columns=scale_cols)
#print(df)

x_train, x_test, y_train, y_test = train_test_split(df.drop('close', axis=1), df['close'], test_size=0.2, random_state=0, shuffle=False)
x_train.shape, y_train.shape
# print(type(x_test))
# print(x_test)
def windowed_dataset(x, y, window_size, batch_size, shuffle):
    # X값 window dataset 구성
    ds_x = tf.data.Dataset.from_tensor_slices(x)
    ds_x = ds_x.window(window_size, shift=1, stride=1, drop_remainder=True)
    ds_x = ds_x.flat_map(lambda x: x.batch(window_size))
    # y값 추가
    ds_y = tf.data.Dataset.from_tensor_slices(y[window_size:])
    ds = tf.data.Dataset.zip((ds_x, ds_y))
    if shuffle:
        ds = ds.shuffle(1000)
    return ds.batch(batch_size).prefetch(1)
WINDOW_SIZE=5
BATCH_SIZE=32
train_data = windowed_dataset(x_train, y_train, WINDOW_SIZE, BATCH_SIZE, True)
test_data = windowed_dataset(x_test, y_test, WINDOW_SIZE, BATCH_SIZE, False)

model = Sequential([
    # 1차원 feature map 생성
    Conv1D(filters=32, kernel_size=5,
           padding="causal",
           activation="relu",
           input_shape=[WINDOW_SIZE, 5]),
    # LSTM
    LSTM(16, activation='tanh'),
    Dense(16, activation="relu"),
    Dense(1),
])

# Sequence 학습에 비교적 좋은 퍼포먼스를 내는 Huber()를 사용합니다.
loss = Huber()
optimizer = Adam(0.0005)
model.compile(loss=loss, optimizer=optimizer, metrics=['mse'])

# earlystopping은 35번 epoch통안 val_loss 개선이 없다면 학습을 멈춥니다.
earlystopping = EarlyStopping(monitor='val_loss', patience=35)

history = model.fit(train_data,
                    validation_data=(test_data),
                    epochs=3,
                    callbacks=[earlystopping])

pred = model.predict(test_data)
actual = np.asarray(y_test)[WINDOW_SIZE:]
actual = np.reshape(actual, (len(actual), 1))

plt.figure(figsize=(10,10))
plt.plot(actual, label='actual')
plt.plot(pred, label='prediction')
plt.legend()
plt.savefig('btc.png')
plt.show()