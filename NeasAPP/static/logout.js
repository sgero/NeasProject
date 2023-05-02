var slider = document.querySelector('.slider');
var images = slider.querySelectorAll('img');
var currentImageIndex = 0;
var interval;

function startSlider() {
  interval = setInterval(() => {
    images[currentImageIndex].classList.remove('active');
    currentImageIndex = (currentImageIndex + 1) % images.length;
    images[currentImageIndex].classList.add('active');
  }, 2000);
}

startSlider();