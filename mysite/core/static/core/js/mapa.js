$(function(){
    if (navigator.geolocation)
    {
        navigator.geolocation.getCurrentPosition(getCoords, getError);
    }else{

    }

    function getCoords(position)
    {
        var lat = position.coords.latitude;
        var lng = position.coords.longitude;
        $('#id_coord_latitude').val(lat);
        $('#id_coord_length').val(lng);
        
        initialize(lat, lng);
    }

    function getError(err)
    {
        initialize(13.30272, -87.194107);
    }

    function initialize(lat, lng)
    {
        var latlng = new google.maps.LatLng(lat,lng);
        var mapSettings = {
            center: latlng,
            zoom: 15,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        }
        
        map = new google.maps.Map($('#mapa').get(0), mapSettings);

        var marker = new google.maps.Marker({
            position: latlng,
            map: map,
            draggable: true,
            title: 'Arrastrame'
        });

        google.maps.event.addListener(marker, 'position_changed', function(){
            getMarkerCoords(marker);
        });
    }

    function getMarkerCoords(marker)
    {
        var markerCoords = marker.getPosition();
        $('#id_coord_latitude').val(markerCoords.lat());
        $('#id_coord_length').val(markerCoords.lng());
    }

    $('#form_coords').submit(function(e){
        e.preventDefault();
        $.post('coordenate/save'),$(this).serialize(), function(data){
        }
    });
});