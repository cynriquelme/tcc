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
        initialize(-25.3342, -57.5373);
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
        if ("{{ report.coord_latitude}}"== null) { 
            $('#id_coord_latitude').val("{{ report.coord_latitude}}");
            $('#id_coord_length').val("{{ report.coord_length}}");
         } else { 
            var markerCoords = marker.getPosition();
            $('#id_coord_latitude').val(markerCoords.lat());
            $('#id_coord_length').val(markerCoords.lng());
         }
    }

    $('#form_coords').submit(function(e){
        e.preventDefault();
        $.post('coordenate/save'),$(this).serialize(), function(data){
        }
    });
});