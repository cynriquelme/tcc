function mostrarPassword(){
    var cambio = document.getElementById("id_password");
    if(cambio.type == "password"){
        cambio.type = "text";
        $('.icon').removeClass('fa fa-eye-slash').addClass('fa fa-eye');
    }else{
        cambio.type = "password";
        $('.icon').removeClass('fa fa-eye').addClass('fa fa-eye-slash');
    }
}

    $(document).ready(function () {
    //CheckBox mostrar contraseña
    $('#ShowPassword').click(function () {
        $('#Password').attr('type', $(this).is(':checked') ? 'text' : 'password');
    });    
});
document.getElementById("id_star_date").value = "";
document.getElementById("id_end_date").value = "";
document.getElementById("id_description").value = "";
document.getElementById("id_type_report").value = "";
document.getElementById("id_sub_category").value = "";