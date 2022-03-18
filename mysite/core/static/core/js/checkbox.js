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
function mostrar(){
    document.getElementById('tr_reward').style.display = 'contents';
}
    
function ocultar(){
    document.getElementById('tr_reward').style.display = 'none';
}

$(document).ready(function () {
    $('#reward').on('checkbox change', function () {
        if (this.checked) {
            mostrar();
        }
        else {
            ocultar();
        }
    });
});

