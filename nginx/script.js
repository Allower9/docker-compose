document.getElementById('fetchData').addEventListener('click', function() {
    fetch('http://localhost:5000/api/data') // Замените на ваш API-эндпоинт
        .then(response => response.json())
        .then(data => {
            document.getElementById('data').innerText = JSON.stringify(data);
        })
        .catch(error => console.error('Ошибка:', error));
});

