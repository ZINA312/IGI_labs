function startCountdown() {
    const countdownElement = document.getElementById('countdown');
    const oneHourInMilliseconds = 60 * 60 * 1000; 
    let endTime;

    const savedEndTime = localStorage.getItem('countdownEndTime');
    if (savedEndTime) {
        endTime = parseInt(savedEndTime);
    } else {
        endTime = Date.now() + oneHourInMilliseconds;
        localStorage.setItem('countdownEndTime', endTime);
    }

    const interval = setInterval(() => {
        const remainingTime = endTime - Date.now();

        if (remainingTime <= 0) {
            clearInterval(interval);
            countdownElement.textContent = "Время вышло!";
            localStorage.removeItem('countdownEndTime'); 
        } else {
            const hours = Math.floor((remainingTime % (1000 * 60 * 60)) / (1000 * 60 * 60));
            const minutes = Math.floor((remainingTime % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((remainingTime % (1000 * 60)) / 1000);
            countdownElement.textContent = `${hours}ч ${minutes}м ${seconds}с`;
        }
    }, 1000);
}

document.addEventListener('DOMContentLoaded', startCountdown);
