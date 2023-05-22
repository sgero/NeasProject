function darLike(comentarioId, usuarioId) {
  console.log('Usuario ID:', usuarioId);
  var csrfToken = $('.btn-like[data-csrf]').data('csrf');
  $.ajax({
    url: '/ruta/detalles/' + comentarioId +'/dar_like/' + usuarioId + '/',
    type: 'POST',
    data: {
      'csrfmiddlewaretoken': csrfToken},
    success: function(response) {

      var likesContador = $('#comentario-' + comentarioId + ' .likes-contador');
      likesContador.text(response.likes_contador);


      var botonLike = $('#comentario-' + comentarioId + ' .btn-like');
      if (response.dio_like) {
        botonLike.find('i').removeClass('far').addClass('fas');
      } else {
        botonLike.find('i').removeClass('fas').addClass('far');
      }
    }
  });
}