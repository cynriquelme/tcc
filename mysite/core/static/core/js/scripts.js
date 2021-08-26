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
    }
});