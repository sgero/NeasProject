let carrusel = document.querySelector('.carrusel-imagenes');
let imagenes = document.querySelectorAll('.imagen');
let index = 0;
setInterval(function() {
    index = (index + 1) % imagenes.length;
    carrusel.style.transform = `translateX(-${index * (100 / imagenes.length)}%)`;
}, 5000);