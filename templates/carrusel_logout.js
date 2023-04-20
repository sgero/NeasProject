var imagenes = ["catedralsevilla.jpg", "giralda.png", "fotosevilla.jpg"];

var carrusel = document.getElementById("carrusel");
for (var i = 0; i < imagenes.length; i++) {
    var imagen = document.createElement("img");
    imagen.src = imagenes[i];
    carrusel.appendChild(imagen);
}

var mensaje = document.createElement("p");
mensaje.innerHTML = "Vuelve pronto a visitarnos";
carrusel.appendChild(mensaje);
