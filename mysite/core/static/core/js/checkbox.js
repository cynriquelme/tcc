$(document).ready(function () {
    $('#terminos').on('checkbox change', function () {
        if (this.checked) {
            $('#btn_registrarse').prop('disabled', false);
        }
        else {
            $('#btn_registrarse').prop('disabled', true);
        }
    });
});
