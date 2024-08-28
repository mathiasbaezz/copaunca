  // JavaScript para resaltar el líder de la tabla
        var tabla = document.getElementById('tabla-posiciones');
        var filas = tabla.getElementsByTagName('tr');
        for (var i = 1; i < filas.length; i++) {
            filas[i].addEventListener('mouseover', function() {
                this.classList.add('highlight');
            });
            filas[i].addEventListener('mouseout', function() {
                this.classList.remove('highlight');
            });
        }


        // Obtén todos los elementos con la clase 'match-time-lapsed'
var elementosTiempo = document.getElementsByClassName('match-time-lapsed');

// Recorre los elementos y agrega los iconos según el tipo de evento
for (var i = 0; i < elementosTiempo.length; i++) {
  var tipoEvento = elementosTiempo[i].getAttribute('data-tipo-evento');

  if (tipoEvento === 'Gol Local' || tipoEvento === 'Gol Visitante') {
    elementosTiempo[i].innerHTML = '<i class="fa fa-soccer-ball-o"></i>' + elementosTiempo[i].innerHTML;
  } else if (tipoEvento === 'Tarjeta Roja Local' || tipoEvento === 'Tarjeta Roja Visitante') {
    elementosTiempo[i].innerHTML = '<i class="fas fa-square redcard-icon"></i>' + elementosTiempo[i].innerHTML;
  }
}


