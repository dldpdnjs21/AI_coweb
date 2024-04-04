const modal = document.getElementById('coinModal');
const closeButton = document.querySelector('.close');

// 모달 닫기
function closeModal() {
    modal.style.display = 'none';
}
closeButton.addEventListener('click', closeModal);



// 코인 클릭 이벤트 리스너 등록
const coinList = document.querySelector('.coinList tbody');
coinList.addEventListener('click', function (event) {
    const clickedCoin = event.target.closest('tr').querySelector('td:first-child').textContent;
    openModal();
});

// 모달 열기
function openModal() {
    modal.style.display = 'block';
}

const Register = document.querySelector('.login-here');

Register.addEventListener('click', (event) => {
    event.preventDefault();
    closeModal();

    const wrapper = document.querySelector('.wrapper');
    wrapper.classList.add('active-popup');

});