    var imagenes = ["/NeasAPP/static/img/catedralsevilla.jpg", "/NeasAPP/static/img/giralda.png", "/NeasAPP/static/img/otosevilla.jpg"];

    var carrusel_logout = document.getElementById("carrusel_logout");
    for (var i = 0; i < imagenes.length; i++) {
        var imagen = document.createElement("img");
        imagen.src = imagenes[i];
        carrusel_logout.appendChild(imagen);
    }

    var mensaje = document.createElement("p");
    mensaje.innerHTML = "Vuelve pronto a visitarnos";
    carrusel_logout.appendChild(mensaje);