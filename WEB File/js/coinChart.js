document.addEventListener('DOMContentLoaded', function () {
    const modal = document.getElementById('coinModal');
    const closeButton = document.querySelector('.close');
    const transactionForm = document.getElementById('transactionForm');
    const quantityInput = document.getElementById('quantity');
    const priceInput = document.getElementById('price');
    const totalInput = document.getElementById('total');
    const transactionTypeSelect = document.getElementById('transactionType');
    const ctx = document.getElementById('coinChart').getContext('2d');

    // 모달 열기
    function openModal() {
        modal.style.display = 'block';
    }

    // 모달 닫기
    function closeModal() {
        modal.style.display = 'none';
    }

    // 모달 닫기 이벤트 처리
    closeButton.addEventListener('click', closeModal);
    window.addEventListener('click', function (event) {
        if (event.target === modal) {
            closeModal();
        }
    });

    // 코인 차트 데이터
    const coinData = {
        labels: ["Bitcoin", "Ethereum", "Dogecoin", "Litecoin", "Cardano", "Ripple", "Polkadot", "Chainlink", "Stellar", "Bitcoin Cash", "Ada", "Tron", "BitTorrent", "Basic Attention Token"],
        prices: [65000000, 2500000, 700, 220000, 2000, 900, 35000, 30000, 400, 700000, 3000, 100, 5, 0.5]
    };

    // 코인 차트 생성
    const coinChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: coinData.labels,
            datasets: [{
                label: 'Price (원)',
                data: coinData.prices,
                backgroundColor: 'rgba(54, 162, 235, 0.5)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    // 코인 거래 폼 제출 처리
    transactionForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const quantity = parseInt(quantityInput.value);
        const price = parseFloat(priceInput.value);
        const total = quantity * price;
        const transactionType = transactionTypeSelect.value;
        totalInput.value = total.toFixed(2);
        // 여기서는 간단히 총액을 계산하여 출력하는 예시로 작성하였습니다.
        // 실제로는 서버로 코인 거래 요청을 전송하고, 처리 결과를 반영해야 합니다.
        console.log(`Quantity: ${quantity}, Price: ${price}, Total: ${total}, Transaction Type: ${transactionType}`);
    });

    // 코인 클릭 시 모달 열기
    const coinList = document.querySelector('.coinList tbody');
    coinList.addEventListener('click', function (event) {
        const clickedCoin = event.target.closest('tr').querySelector('td:first-child').textContent;
        openModal();
        console.log(`Clicked Coin: ${clickedCoin}`);
        // 여기에 선택된 코인에 관련된 정보를 모달에 표시하는 코드를 추가할 수 있습니다.
    });
});
