document.addEventListener("DOMContentLoaded", function() {
    const apiUrls = {
        ticker: "https://api.upbit.com/v1/ticker?markets=KRW-BTC,KRW-ETH,KRW-XRP,KRW-STX",
    };

    let candleChart = {};

    let selectedCoin = "";

    function drawCandleChartForSelectedCoin(data) {
        const coin = data.find(coin => coin.market === selectedCoin);
        if (coin) {
            const coinName = coin.market;
            const price = coin.trade_price;
            drawCandleChart(coinName, price);
        }
    }

    // 분봉 차트 그리기
    setInterval(() => {
        fetchTickerData()
            .then(data => {
                console.log("Real-time Ticker Data:", data);
                drawCandleChartForSelectedCoin(data);
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation for ticker:', error);
            });
    }, 1000);

    function fetchTickerData() {
        return fetch(apiUrls.ticker)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            });
    }

    // 분봉 차트 그리기
    function drawCandleChart(coinName, price) {
        if (!candleChart[coinName]) {
            const ctx = document.getElementById('candle-chart').getContext('2d');
            const initialData = {
                labels: [coinName],
                datasets: [{
                    label: [coinName],
                    data: [],
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1
                }]
            };
            candleChart[coinName] = new Chart(ctx, {
                type: 'line',
                data: initialData,
                options: {
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true,
                                stepSize:500
                            }
                        }]
                    }
                }
            });
        }

        const currentTime = new Date().toLocaleTimeString();
        if (candleChart[coinName].data.labels.length >= 10) {
            candleChart[coinName].data.labels.shift();
            candleChart[coinName].data.datasets[0].data.shift();
        }

        candleChart[coinName].data.labels.push(currentTime);
        candleChart[coinName].data.datasets[0].data.push(price);

        candleChart[coinName].update();
    }

    document.querySelector('.coinList tbody').addEventListener('click', function(event) {
        const clickedCoin = event.target.closest('tr').querySelector('td:first-child').textContent;
        selectedCoin = clickedCoin;

        Object.values(candleChart).forEach(chart => chart.destroy());
        candleChart = {};

        fetchTickerData()
            .then(data => {
                console.log("Real-time Ticker Data:", data);
                drawCandleChartForSelectedCoin(data);
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation for ticker:', error);
            });

    });
});
