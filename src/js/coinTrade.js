document.addEventListener("DOMContentLoaded", function() {
    // API 주소 설정
    const apiUrl = "https://api.upbit.com/v1/ticker?markets=KRW-BTC";

    // 사용자가 원화로 BTC를 10만원 구매한 가정
    let buyPrice = 100000;

    // 초기화
    fetchAndDisplayData();

    // 주기적으로 데이터 업데이트
    setInterval(fetchAndDisplayData, 1000);

    function fetchAndDisplayData() {
        // BTC의 실시간 시세 가져오기
        fetch(apiUrl)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                // BTC의 현재 가격 가져오기
                let btcPrice = data[0]['trade_price'];

                // BTC 수량 계산
                let btcQuantity = buyPrice / btcPrice;

                // 매수금액, 평가손익, 평가금액, 평가 수익률 계산
                let totalInvestment = buyPrice;
                let currentInvestment = buyPrice;
                let profitLoss = 0;
                let evaluationRate = 0;

                // HTML 업데이트
                document.getElementById("buyPrice").innerText = formatPrice(buyPrice);
                document.getElementById("btcQuantity").innerText = formatBtcQuantity(btcQuantity);
                document.getElementById("currentInvestment").innerText = formatPrice(currentInvestment);
                document.getElementById("profitLoss").innerText = formatPrice(profitLoss);
                document.getElementById("evaluationRate").innerText = formatPercent(evaluationRate);
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
            });
    }

    // 가격을 형식화하는 함수
    function formatPrice(price) {
        return price.toLocaleString() + " KRW";
    }

    // BTC 수량을 형식화하는 함수
    function formatBtcQuantity(quantity) {
        return quantity.toFixed(8) + " BTC";
    }

    // 퍼센트를 형식화하는 함수
    function formatPercent(percent) {
        return percent.toFixed(2) + "%";
    }
});
