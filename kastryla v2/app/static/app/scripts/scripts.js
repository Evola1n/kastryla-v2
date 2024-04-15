// Проверяем, есть ли сохраненная тема в localStorage и применяем ее
document.addEventListener('DOMContentLoaded', (event) => {
    if (localStorage.getItem('theme') === 'dark') {
        document.body.classList.add('dark-theme');
        document.getElementById('theme-toggle').checked = true;
    }
});

// Слушатель для переключателя темы
document.getElementById('theme-toggle').addEventListener('change', function (event) {
    if (event.target.checked) {
        document.body.classList.add('dark-theme');
        localStorage.setItem('theme', 'dark'); // Сохраняем выбор темы
    } else {
        document.body.classList.remove('dark-theme');
        localStorage.setItem('theme', 'light'); // Сохраняем выбор темы
    }
});

const chk = document.getElementById('chk');

function orderProduct(productName) {
    // Открываем новую вкладку с формой для заполнения
    var win = window.open('/order/?product=' + encodeURIComponent(productName), 'order');
}



