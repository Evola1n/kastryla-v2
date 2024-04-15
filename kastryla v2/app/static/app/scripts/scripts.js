// ���������, ���� �� ����������� ���� � localStorage � ��������� ��
document.addEventListener('DOMContentLoaded', (event) => {
    if (localStorage.getItem('theme') === 'dark') {
        document.body.classList.add('dark-theme');
        document.getElementById('theme-toggle').checked = true;
    }
});

// ��������� ��� ������������� ����
document.getElementById('theme-toggle').addEventListener('change', function (event) {
    if (event.target.checked) {
        document.body.classList.add('dark-theme');
        localStorage.setItem('theme', 'dark'); // ��������� ����� ����
    } else {
        document.body.classList.remove('dark-theme');
        localStorage.setItem('theme', 'light'); // ��������� ����� ����
    }
});

const chk = document.getElementById('chk');

function orderProduct(productName) {
    // ��������� ����� ������� � ������ ��� ����������
    var win = window.open('/order/?product=' + encodeURIComponent(productName), 'order');
}



