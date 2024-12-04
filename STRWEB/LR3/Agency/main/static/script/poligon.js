const toggleControls = document.getElementById('toggleControls');
const controls = document.getElementById('controls');
const fontSizeSelect = document.getElementById('fontSize');
const textColorInput = document.getElementById('textColor');
const bgColorInput = document.getElementById('bgColor');

toggleControls.addEventListener('change', () => {
    controls.style.display = toggleControls.checked ? 'block' : 'none';
});

fontSizeSelect.addEventListener('change', () => {
    document.body.style.fontSize = fontSizeSelect.value;
});

textColorInput.addEventListener('input', () => {
    document.body.style.color = textColorInput.value;
});

bgColorInput.addEventListener('input', () => {
    document.body.style.backgroundColor = bgColorInput.value;
});

document.getElementById('checkAge').addEventListener('click', () => {
    const birthDateInput = document.getElementById('birthDate').value;
    if (!birthDateInput) {
        alert('Пожалуйста, введите дату рождения.');
        return;
    }

    const birthDate = new Date(birthDateInput);
    const today = new Date();
    const age = today.getFullYear() - birthDate.getFullYear();
    const monthDiff = today.getMonth() - birthDate.getMonth();
    const dayDiff = today.getDate() - birthDate.getDate();

    const isMinor = age < 18 || (age === 18 && (monthDiff < 0 || (monthDiff === 0 && dayDiff < 0)));
    if(birthDate > today){
        alert('Неверная дата');
        return;
    }
    if (isMinor) {
        alert('Вам необходимо разрешение родителей на использование этого сайта.');
    } else {
        const daysOfWeek = ['Воскресенье', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота'];
        const dayOfWeek = daysOfWeek[birthDate.getDay()];
        document.getElementById('ageMessage').textContent = `Вы совершеннолетний. Ваш день рождения был в ${dayOfWeek}. Вам ${age} лет.`;
    }
});

// //вариант 2
// class DateObject {
//     constructor(day, month, year) {
//         this.day = day;
//         this.month = month;
//         this.year = year;
//     }

//     isSpring() {
//         return this.month >= 3 && this.month <= 5; // Март, Апрель, Май
//     }

//     toString() {
//         return `${this.day}/${this.month}/${this.year}`;
//     }
// }

// // Массив для хранения объектов дат
// const dateArray = [
//     new DateObject(15, 3, 2023),
//     new DateObject(10, 6, 2023),
//     new DateObject(5, 4, 2023),
//     new DateObject(20, 11, 2023)
// ];

// // Функция для отображения весенних дат
// document.getElementById('showSpringDates').addEventListener('click', () => {
//     const springDatesList = document.getElementById('springDatesList');
//     springDatesList.innerHTML = ''; // Очистить предыдущий список

//     const springDates = dateArray.filter(date => date.isSpring());
//     springDates.forEach(date => {
//         const li = document.createElement('li');
//         li.textContent = date.toString();
//         springDatesList.appendChild(li);
//     });

//     if (springDates.length === 0) {
//         springDatesList.innerHTML = '<li>Нет весенних дат.</li>';
//     }
// });

//вариант 1
function DateObject(day, month, year) {
    this.day = day;
    this.month = month;
    this.year = year;
}

// Метод для проверки весенней даты
DateObject.prototype.isSpring = function() {
    return this.month >= 3 && this.month <= 5;
};

// Метод для отображения даты
DateObject.prototype.toString = function() {
    return `${this.day}/${this.month}/${this.year}`;
};

// Массив для хранения объектов дат
const dateArray = [
    new DateObject(15, 3, 2023),
    new DateObject(10, 6, 2023),
    new DateObject(5, 4, 2023),
    new DateObject(20, 11, 2023)
];

// Функция для отображения весенних дат
document.getElementById('showSpringDates').addEventListener('click', () => {
    const springDatesList = document.getElementById('springDatesList');
    springDatesList.innerHTML = ''; 

    const springDates = dateArray.filter(date => date.isSpring());
    springDates.forEach(date => {
        const li = document.createElement('li');
        li.textContent = date.toString();
        springDatesList.appendChild(li);
    });

    if (springDates.length === 0) {
        springDatesList.innerHTML = '<li>Нет весенних дат.</li>';
    }
});

// Функция для создания файла и скачивания
function downloadSpringDates(dates) {
    const springDates = dates.filter(date => date.isSpring());
    const content = springDates.map(date => date.toString()).join('\n');

    const blob = new Blob([content], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'spring_dates.txt';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}

// Добавим обработчик для кнопки скачивания
document.getElementById('showSpringDates').addEventListener('click', () => {
    const springDatesList = document.getElementById('springDatesList');
    springDatesList.innerHTML = '';

    const springDates = dateArray.filter(date => date.isSpring());
    springDates.forEach(date => {
        const li = document.createElement('li');
        li.textContent = date.toString();
        springDatesList.appendChild(li);
    });

    if (springDates.length === 0) {
        springDatesList.innerHTML = '<li>Нет весенних дат.</li>';
    } else {
        downloadSpringDates(dateArray);
    }
});

// Данные для графиков
const xValues = [...Array(100).keys()].map(x => x / 100 - 0.5); // от -0.5 до 0.49
const seriesData = xValues.map(x => {
    let sum = 0;
    for (let n = 0; n < 10; n++) { // Пример с 10 членами ряда
        sum += Math.pow(-1, n) * Math.pow(x, n + 1) / (n + 1);
    }
    return sum;
});

const mathFunctionData = xValues.map(x => Math.log(1 + x)); // Функция ln(1+x)

// Создание графика
const ctx = document.getElementById('myChart').getContext('2d');
const myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: xValues,
        datasets: [
            {
                label: 'Разложение в ряд',
                data: seriesData,
                borderColor: 'rgba(75, 192, 192, 1)',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                fill: false
            },
            {
                label: 'ln(1+x)',
                data: mathFunctionData,
                borderColor: 'rgba(255, 99, 132, 1)',
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                fill: false
            }
        ]
    },
    options: {
        responsive: true,
        scales: {
            x: {
                title: {
                    display: true,
                    text: 'x'
                }
            },
            y: {
                title: {
                    display: true,
                    text: 'F(x)'
                }
            }
        },
        plugins: {
            legend: {
                display: true,
                position: 'top'
            },
            annotation: {
                annotations: {
                    line1: {
                        type: 'line',
                        yMin: 0,
                        yMax: 0,
                        xMin: -0.5,
                        xMax: 0.5,
                        borderColor: 'red',
                        borderWidth: 2,
                        label: {
                            content: 'y = 0',
                            enabled: true,
                            position: 'top'
                        }
                    }
                }
            }
        }
    }
});

// Функция для скачивания графика
document.getElementById('downloadBtn').addEventListener('click', function() {
    const link = document.createElement('a');
    link.href = myChart.toBase64Image();
    link.download = 'chart.png'; 
    link.click();
});