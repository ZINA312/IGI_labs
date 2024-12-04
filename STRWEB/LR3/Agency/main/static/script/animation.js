document.addEventListener("DOMContentLoaded", () => {
    const scrollingHouses = document.getElementById("scrolling-houses");

    // Добавляем изображения домов
    const house1 = document.createElement("img");
    house1.src = "/static/houses/house1.png"; 
    house1.alt = "Дом 1";
    house1.classList.add("house-img");

    const house2 = document.createElement("img");
    house2.src = "/static/houses/house2.png"; 
    house2.alt = "Дом 2";
    house2.classList.add("house-img");

    scrollingHouses.appendChild(house1);
    scrollingHouses.appendChild(house2);

    // Функция для обновления прозрачности
    const updateOpacity = () => {
        const scrollTop = window.scrollY; // Текущая вертикальная прокрутка
        const documentHeight = document.body.scrollHeight - window.innerHeight; // Высота прокрутки страницы
        const scrollFraction = scrollTop / documentHeight; // Доля прокрутки (от 0 до 1)

        const opacity = scrollFraction; // Прозрачность: 1 наверху, 0 внизу
        scrollingHouses.style.opacity = opacity.toFixed(2); 
    };

    updateOpacity();
    window.addEventListener("scroll", updateOpacity);
});