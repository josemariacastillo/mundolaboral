% include('header.tpl', title='MundoLaboral ')
    
    <div id="map"  class="map"></div>
    
    <script type="text/javascript">
      var key = "AIzaSyA3tPw8KWXy1diMpgStWOgtza_uixiUuzw";
      var url = "https://maps.googleapis.com/maps/api/geocode/json";
      var parameters = {};
      var ciudades = {{!ci}};
      
      function initMap() {
        window.map = new google.maps.Map(document.getElementById('map'), {
              center: {lat: 40.4167754, lng: -3.7037902},
              zoom: 5
            });
        for(c in ciudades){
          parameters = {address : c}
          
          $.getJSON(url, parameters, function(data,textStatus,jqXHR){
            if(data.status == 'OK'){

              var myLatlng = new google.maps.LatLng(data.results[0].geometry.location.lat,data.results[0].geometry.location.lng);
              var marker = new google.maps.Marker({
                  position: myLatlng,
                  animation: google.maps.Animation.DROP,
                  title:data.results[0].address_components[0].short_name
              });
              // To add the marker to the map, call setMap();
              marker.setMap(map);
              google.maps.event.addListener(marker, 'click', function() {
                ofertas = ciudades[this.toString()];
                var texto = '<ul>';
                if(ofertas){
                  for(o in ofertas){
                    texto+='<li><a href="'+ofertas[o].url+'" target="_blank">'+ofertas[o].titulo+'</a></li>';
                  }
                }
                texto+='</ul>';
                var infoWindow = new google.maps.InfoWindow({content: texto});
                infoWindow.open(map, marker);
              }.bind(this));
            }
          }.bind(c));  
        }
      }

    </script>
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyA3tPw8KWXy1diMpgStWOgtza_uixiUuzw&signed_in=true&callback=initMap"
        async defer>
    </script>
% include('footer.tpl')
