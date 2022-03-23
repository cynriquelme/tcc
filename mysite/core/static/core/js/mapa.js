$(function(){
    if (navigator.geolocation)
    {    
        if($('#id_latitude_update').val()!==undefined){
            var latU =  $('#id_latitude_update').val();
            var lngU = $('#id_length_update').val();  
            initializeUpdate(latU, lngU);
        }else{
            navigator.geolocation.getCurrentPosition(getCoords, getError);
            var latR =  document.getElementById("location_lat").textContent;
            var lngR = document.getElementById("location_len").textContent;
            initializeReport(latR, lngR);
        }
    }else{
        alert("La ubicación no está activada..");
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
        initialize(-25.40, -57.30);
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

    function initializeUpdate(latU, lngU)
    {
        var latlng = new google.maps.LatLng(latU,lngU);
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

    
    function initializeReport(latR, lngR)
    {
        var latlng = new google.maps.LatLng(latR,lngR);
        var mapSettings = {
            center: latlng,
            zoom: 15,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        }
        
        map = new google.maps.Map($('#map').get(0), mapSettings);

        var marker = new google.maps.Marker({
            position: latlng,
            map: map,
            title: 'Ubicación marcada del Reporte',
            animation: google.maps.Animation.DROP
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
        $('#id_latitude_update').val(markerCoords.lat());
        $('#id_length_update').val(markerCoords.lng());    
    }

    $('#form_coords').submit(function(e){
        e.preventDefault();
        $.post('coordenate/save'),$(this).serialize(), function(data){
        }
    });
});
