$(document).ready(function () {
    // Agregar animación a los campos de formulario
    $(".contenedor-formularios").find("input, textarea").on("keyup blur focus", function (e) {
        var $this = $(this),
            label = $this.prev("label");
        if (e.type === "keyup") {
            if ($this.val() === "") {
                label.removeClass("active highlight");
            } else {
                label.addClass("active highlight");
            }
        } else if (e.type === "blur") {
            if ($this.val() === "") {
                label.removeClass("active highlight");
            } else {
                label.removeClass("highlight");
            }
        } else if (e.type === "focus") {
            if ($this.val() === "") {
                label.removeClass("highlight");
            } else if ($this.val() !== "") {
                label.addClass("highlight");
            }
        }
    });

    $(document).ready(function () {
        $('form').submit(function (event) {
            var password1 = $('#password1').val();
            var password2 = $('#password2').val();

            if (password1 !== password2) {
                alert('Las contraseñas no coinciden');
                event.preventDefault();
            }
        });
    });
});