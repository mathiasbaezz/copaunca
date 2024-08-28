$(document).ready(function() {
    $("#newsletter").on('submit', function (e) {
        e.preventDefault();
        var emailUsuario = $("#emailUsuario").val();
        if (emailUsuario == "") {
            Swal.fire({
                title: 'Error!',
                text: 'Por favor ingrese su correo para suscribirse al newsletter',
                type: 'error',
                confirmButtonText: 'De Acuerdo'
            });
        } else {
            $.ajax({
                url: "/correo",
                data: {
                    emailUsuario: emailUsuario,
                    csrfmiddlewaretoken: window.CSRF_TOKEN
                },
                dataType: 'json',
                type: 'POST',
                success: function (data) {
                    if (data.success) {
                        $("#emailUsuario").val("");
                        Swal.fire(
                            'Listo',
                            '¡Ya estás suscrito al newsletter!',
                            'success'
                        );
                    } else {
                        Swal.fire({
                            title: 'Error!',
                            text: 'Ha ocurrido un error. Por favor, intenta nuevamente.',
                            type: 'error',
                            confirmButtonText: 'De Acuerdo'
                        });
                    }
                },
                error: function (xhr, status, error) {
                    console.log(xhr.responseText);
                }
            });
        }
    });
});