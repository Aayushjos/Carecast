// JavaScript for automatic sliding
const slider = document.querySelector('.slider');
const slides = document.querySelectorAll('.slide');

let slideIndex = 1;

function showSlide(n) {
    if (n < 1) {
        slideIndex = slides.length;
    } else if (n > slides.length) {
        slideIndex = 1;
    }

    slides.forEach((slide) => (slide.style.display = 'none'));
    slides[slideIndex - 1].style.display = 'block';
}

function changeSlide(n) {
    showSlide((slideIndex += n));
}

function autoSlide() {
    changeSlide(1);
}

setInterval(autoSlide, 4000); // Change the time interval to 8000 milliseconds (8 seconds)
showSlide(slideIndex);


