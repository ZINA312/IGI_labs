class Slider {
    constructor(sliderElement, options = {}) {
        this.sliderElement = sliderElement;
        this.slides = sliderElement.querySelector('.slides');
        this.slideElements = Array.from(this.slides.children);
        this.currentIndex = 0;
        this.autoPlay = options.auto ?? true;
        this.autoPlayDelay = options.delay ? options.delay * 1000 : 5000;
        this.loop = options.loop ?? true;
        this.showNavs = options.navs ?? true;
        this.showPags = options.pags ?? true;
        this.stopMouseHover = options.stopMouseHover ?? false;
        
        // Новый элемент для отображения номера слайда
        this.slideNumberElement = document.createElement('div');
        this.slideNumberElement.style.position = 'absolute';
        this.slideNumberElement.style.top = '10px'; 
        this.slideNumberElement.style.left = '10px';
        this.slideNumberElement.style.color = 'white';
        this.slideNumberElement.style.fontSize = '1.2rem';
        this.sliderElement.appendChild(this.slideNumberElement);
        
        this.init();
    }

    init() {
        this.updatePagination();
        this.updateSlideNumber(); // Обновляем номер слайда при инициализации
        this.setupEventListeners();
        if (this.autoPlay) {
            this.startAutoPlay();
        }
        this.toggleNavs();
        this.togglePags();
    }

    setupEventListeners() {
        if (this.showNavs) {
            this.sliderElement.querySelector('#prev').addEventListener('click', () => this.prevSlide());
            this.sliderElement.querySelector('#next').addEventListener('click', () => this.nextSlide());
        }
        
        if (this.showPags) {
            this.slideElements.forEach((slide, index) => {
                const button = document.createElement('button');
                button.innerText = index + 1;
                button.addEventListener('click', () => this.goToSlide(index));
                this.sliderElement.querySelector('#pagination').appendChild(button);
            });
        }

        if (this.stopMouseHover) {
            this.sliderElement.addEventListener('mouseover', () => this.stopAutoPlay());
            this.sliderElement.addEventListener('mouseout', () => this.startAutoPlay());
        }
    }

    startAutoPlay() {
        this.autoPlayInterval = setInterval(() => this.nextSlide(), this.autoPlayDelay);
    }

    stopAutoPlay() {
        clearInterval(this.autoPlayInterval);
    }

    goToSlide(index) {
        this.currentIndex = index;
        this.updateSlides();
        this.updatePagination();
        this.updateSlideNumber(); 
    }

    nextSlide() {
        this.currentIndex = (this.currentIndex + 1) % this.slideElements.length;
        if (this.currentIndex === 0 && !this.loop) {
            this.stopAutoPlay();
        }
        this.updateSlides();
        this.updatePagination();
        this.updateSlideNumber(); 
    }

    prevSlide() {
        this.currentIndex = (this.currentIndex - 1 + this.slideElements.length) % this.slideElements.length;
        this.updateSlides();
        this.updatePagination();
        this.updateSlideNumber(); 
    }

    updateSlides() {
        const offset = -this.currentIndex * 100;
        this.slides.style.transform = `translateX(${offset}%)`;
        this.slideElements.forEach((slide, index) => {
            slide.style.opacity = index === this.currentIndex ? 1 : 0;
        });
    }

    updatePagination() {
        const buttons = this.sliderElement.querySelectorAll('#pagination button');
        buttons.forEach((button, index) => {
            button.style.fontWeight = index === this.currentIndex ? 'bold' : 'normal';
        });
    }

    updateSlideNumber() {
        this.slideNumberElement.textContent = `${this.currentIndex + 1}/${this.slideElements.length}`;
    }

    toggleNavs() {
        const nav = this.sliderElement.querySelector('.nav');
        nav.style.display = this.showNavs ? 'flex' : 'none';
    }

    togglePags() {
        const pagination = this.sliderElement.querySelector('.pagination');
        pagination.style.display = this.showPags ? 'flex' : 'none';
    }
}

const sliderOptions = {
    auto: true,
    delay: 5,
    loop: true,
    navs: true,
    pags: true,
    stopMouseHover: true
};

document.addEventListener('DOMContentLoaded', function() {
    const slider = new Slider(document.getElementById('slider'), sliderOptions);
});