document.addEventListener("DOMContentLoaded", function() {
    const apiUrls = {
        marketAll: "https://api.upbit.com/v1/market/all?isDetails=true",
        ticker: "https://api.upbit.com/v1/ticker?markets=KRW-BTC,KRW-ETH,KRW-XRP",
    };

    // 데이터를 가져와서 화면을 업데이트하는 함수를 주기적으로 호출
    setInterval(fetchAndDisplayData, 1000); // 1초마다 업데이트

    // 초기화
    fetchAndDisplayData();

    function fetchAndDisplayData() {
        fetchMarketData()
            .then(data => {
                console.log("Market All Data:", data);
                displayMarketAllData(data);
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation for marketAll:', error);
            });

        fetchTickerData()
            .then(data => {
                console.log("Ticker Data:", data);
                displayTickerData(data);
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation for ticker:', error);
            });
    }

    function fetchMarketData() {
        return fetch(apiUrls.marketAll)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            });
    }

    function fetchTickerData() {
        return fetch(apiUrls.ticker)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            });
    }

    // function displayMarketAllData(data) {
    //     const tbody = document.querySelector('.coinList tbody');
    //
    //     tbody.innerHTML = '';
    //
    //     data.forEach(coin => {
    //         if (coin.market === 'KRW-XRP' || coin.market === 'KRW-ETH' || coin.market === 'KRW-BTC') {
    //             const newRow = document.createElement('tr');
    //             newRow.innerHTML = `
    //                 <td>${coin.korean_name || 'N/A'}</td>
    //                 <td>${formatPrice(coin.trade_price)}</td>
    //                 <td>${formatPercent(coin.signed_change_rate)}</td>
    //                 <td>${formatPrice(coin.acc_trade_price)}</td>
    //             `;
    //             tbody.appendChild(newRow);
    //         }
    //     });
    // }

    function displayTickerData(data) {
        console.log("Ticker Data Received:", data);

        data.forEach(coin => {
            const tickerTable = document.querySelector('.coinList');

            if (tickerTable && (coin.market === 'KRW-BTC' || coin.market === 'KRW-ETH' || coin.market === 'KRW-XRP')) {
                console.log("Coin Data:", coin);
                const coinElement = tickerTable.querySelector(`#${coin.market}`);

                if (!coinElement) {
                    const newRow = document.createElement('tr');
                    newRow.id = coin.market;
                    newRow.innerHTML = `
                        <td>${coin.market}</td>
                        <td>${formatPrice(coin.trade_price)}</td>
                        <td>${formatPercent(coin.signed_change_rate)}</td>
                        <td>${formatPrice(coin.acc_trade_price)}</td>
                    `;
                    tickerTable.querySelector('tbody').appendChild(newRow);
                } else {
                    coinElement.innerHTML = `
                        <td>${coin.market}</td>
                        <td>${formatPrice(coin.trade_price)}</td>
                        <td>${formatPercent(coin.signed_change_rate)}</td>
                        <td>${formatPrice(coin.acc_trade_price)}</td>
                    `;
                }
            } else {
                console.error("Ticker Table Element not found.");
            }
        });
    }

    // 가격을 형식화하는 함수
    function formatPrice(price) {
        if (price !== undefined && price !== null) {
            return price.toLocaleString();
        } else {
            return "N/A";
        }
    }

    // 퍼센트를 형식화하는 함수
    function formatPercent(percent) {
        if (percent !== undefined && percent !== null) {
            return percent.toFixed(2) + "%";
        } else {
            return "N/A";
        }
    }
});
