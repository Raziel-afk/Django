document.addEventListener('DOMContentLoaded', function() {
    console.log('Блог Робинзона Крузо загружен!');
    
    // Пример простого скрипта
    const links = document.querySelectorAll('nav a');
    links.forEach(link => {
        link.addEventListener('click', function() {
            console.log('Переход по ссылке: ' + this.textContent);
        });
    });
});