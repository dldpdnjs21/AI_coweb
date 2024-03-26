//검색창 기능
document.getElementById('search').addEventListener('input', function() {
    const searchInput = this.value.toLowerCase(); // 검색어를 소문자로 변환
    const rows = document.querySelectorAll('.coinList tbody tr');

    rows.forEach(row => {
        const coinName = row.querySelector('td:first-child').textContent.toLowerCase();
        // 검색어와 코인 이름 비교
        if (coinName.includes(searchInput)) {
            row.style.display = 'table-row'; // 일치하는 경우 행 표시
        } else {
            row.style.display = 'none'; // 일치하지 않는 경우 행 숨김
        }
    });
    // 검색 결과가 없을 경우 빈 행을 추가하여 테이블 크기를 유지
    if (!found) {
        const tbody = document.querySelector('.coinList tbody');
        const emptyRow = document.createElement('tr');
        emptyRow.innerHTML = '<td colspan="4" class="empty-row"></td>';
        tbody.appendChild(emptyRow);
    }
});

//Price 내림차순 정렬
const sortPriceDescBtn = document.querySelector('#sort-price-desc');
sortPriceDescBtn.addEventListener('click', function() {
    sortRowsByPrice('descending');
});

//Price 오름차순 정렬
const sortPriceAscBtn = document.querySelector('#sort-price-asc');
sortPriceAscBtn.addEventListener('click', function() {
    sortRowsByPrice('ascending');
});

//Range 내림차순 정렬
const sortRangeDescBtn = document.querySelector('#sort-range-desc');
sortRangeDescBtn.addEventListener('click', function() {
    sortRowsByRange('descending');
});

//Range 오름차순 정렬
const sortRangeAscBtn = document.querySelector('#sort-range-asc');
sortRangeAscBtn.addEventListener('click', function() {
    sortRowsByRange('ascending');
});

//Price 기준
function sortRowsByPrice(order) {
    const tbody = document.querySelector('.coinList tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));

    rows.sort((rowA, rowB) => {
        const priceA = parseFloat(rowA.querySelector('td:nth-child(2)').textContent.replace('원', '').replace(/,/g, ''));
        const priceB = parseFloat(rowB.querySelector('td:nth-child(2)').textContent.replace('원', '').replace(/,/g, ''));

        if (order === 'descending') {
            return priceB - priceA;
        } else {
            return priceA - priceB;
        }
    });

    tbody.innerHTML = '';
    rows.forEach(row => {
        tbody.appendChild(row);
    });
}

//Range 기준
function sortRowsByRange(order) {
    const tbody = document.querySelector('.coinList tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));

    rows.sort((rowA, rowB) => {
        const rangeA = parseFloat(rowA.querySelector('td:nth-child(3)').textContent.replace('%', ''));
        const rangeB = parseFloat(rowB.querySelector('td:nth-child(3)').textContent.replace('%', ''));

        if (order === 'descending') {
            return rangeB - rangeA;
        } else {
            return rangeA - rangeB;
        }
    });

    tbody.innerHTML = '';
    rows.forEach(row => {
        tbody.appendChild(row);
    });
}
