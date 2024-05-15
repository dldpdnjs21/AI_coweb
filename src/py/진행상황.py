'''

History

2024 04 04 비트코인 캔들차트 1분, 60분, 1일 생성
2024 04 05
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

2024 04 07 AI 학습시킬 Api_Learning.py에 csv파일 정리 1~2번항목 (석유시세, 금가격) 까지 정리(github 개재)
2024 04 08 학습시킬 Api_Learning.py에 csv파일 정리 3번항목

문제점
https://wikidocs.net/173005 를 참고하여
RNN 신경망으로 하루를 예측해보려했는데 한달데이터로 하루를 예측하는게 가능한것인가 라는생각이듬
n달전데이터로 그다음달 에측-> 다음달 시가 예측 -> 코인인데 의미없다 판단
또 shape호출결과 df데이터가 부족할것이라고 판단
한달주기데이터X, 일일주기데이터로 변환 필요

2024 04 10 AI학습 고민중 csv데이터를 일별로 변환해야된다고 판단 후 변환중
2024 04 11 프로젝트팀에게 csv를 일별로 변환한다고 상의 후 Coin.csv를 일별로 변환후 다시 merge진행
2024 04 12 csv Kospi추가 후 일별 변환 완료 및 딥러닝 진행
2024 04 15 코인의 하루데이터도 의미없다고 판단, 원활한 데이터처리와 캔들차트삽입을 위해 분당데이터로만 처리
일단 pyupbit에서 지원하는 KRW-BTC의 가격만을 분당데이터로 호출하여 학습시도했지만 대용량 데이터호출에 시간이 엄청걸리고 그마저도 호출이 안되는상황이 발생.

조원들의 사정으로인해 2주동안 휴무

2024 04 30 분당 데이터호출 되는지 확인, count가 150만개가 아닌 최소200만개는 되야 될것 같다 라고 판단 및 pickle사용으로 csv,json보다 더 적은 용량과 메모리로 동작할 수 있게 설정해보려함.
참고 https://github.com/mverleg/array_storage_benchmark, https://wikidocs.net/163288
github에 pickle등재 및 호출 되는지 테스트

개인사정으로 10일정도 휴무

2024 05 12~14 gitclone사용 및 github연동 후 200만개의 데이터를 lts사용으로 github에 등재하려 했지만 실패
DataFrame을 100만개씩 분할 등록시켜 concat하는 방식으로 진행하여 학습할 DataFrame완성
2024 05 15 완성시킨 DataFrame으로 AI학습(LSTM) 진행
문제점
1. 20%를 학습데이터로 나눠 학습을 진행하였는데 데이터가 너무 큰 관계로 1ephoc에 60s가 걸려버린다.(너무시간이 오래걸림)
2. UserWarning: Your input ran out of data; interrupting training. Make sure that your dataset or generator can generate at least `steps_per_epoch * epochs` batches. You may need to use the `.repeat()` function when building your dataset.
  self.gen.throw(value)
입력한 데이터가 부족합니다. 훈련을 중단합니다. 데이터 세트 또는 생성기가 최소한 `steps_per_epoch * epochs` 배치를 생성할 수 있는지 확인하세요.
데이터세트를 구축할 때 `.repeat()` 함수를 사용해야 할 수도 있습니다.
모델 훈련중에 데이터부족 문제가 발생한다(원인을 모르겠다)
3. Local rendezvous is aborting with status: OUT_OF_RANGE: End of sequence
TensorFlow의 데이터셋 처리 과정에서 데이터가 끝에 도달했음에도 불구하고 추가 데이터를 요구할 때 발생할 수 있습니다.
이는 데이터셋의 끝에 도달하여 더 이상 읽을 데이터가 없는 경우에 발생합니다.
모델 훈련중에 데이터부족 문제가 발생한다(원인을 모르겠다22)
'''
