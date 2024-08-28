        window.CSRF_TOKEN = "{{ csrf_token }}"
        $("#contacto").on('submit', function (e) {
            e.preventDefault()
            var contactoUsuario = $("#contactoUsuario").val()
            var contactoNombre = $("#contactoNombre").val()
            var contactoAsunto = $("#contactoAsunto").val()
            var contactoMen = $("#contactoMen").val()

            if( contactoUsuario,
                contactoNombre,
                contactoAsunto,
                contactoMen == ""){
                Swal.fire({
                  title: 'Error!',
                  text: 'Por favor ingrese sus datos en los campos requeridos',
                  type: 'error',
                  confirmButtonText: 'De Acuerdo'
                })
            }else {
                $.ajax({
                    url: "/contacto",
                    data: { contactoUsuario: contactoUsuario,
                            contactoNombre: contactoNombre,
                            contactoAsunto: contactoAsunto,
                            contactoMen: contactoMen,
                            csrfmiddlewaretoken: window.CSRF_TOKEN
                    }, //form
                    dataType: 'json',
                    type: 'POST',
                    success: function (data) {
                      if (data.is_taken) {
                        alert(data.error_message);
                      }
                      $("#contactoUsuario").val("")
                      $("#contactoNombre").val("")
                      $("#contactoAsunto").val("")
                      $("#contactoMen").val("")
                      Swal.fire(
                          'Listo',
                          'Se envio su consulta!',
                          'success'
                      )
                    }
                })
            }
        })