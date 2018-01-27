'use strict';
let button = document.getElementsByTagName('button')[0];
let googleMap = document.getElementsByTagName('iframe')[0];
    
function getPosition() {
  let inputCity = document.getElementById('position').value;
  
  let httpRequest = new XMLHttpRequest();

  httpRequest.open('GET', 'https://devru-latitude-longitude-find-v1.p.mashape.com/latlon.php?location=' + inputCity, true);
  httpRequest.setRequestHeader('X-Mashape-Key', 'kNZCeFC5Otmsh0OnupPCIpQNkck7p18x6A3jsnHrkaW8Bpum8V');
  httpRequest.setRequestHeader('Accept', 'application/json');
  httpRequest.send();
  httpRequest.onreadystatechange = console.log;

  httpRequest.onload = function() {

    if (httpRequest.status >= 200 && httpRequest.status < 400){

      let text = JSON.parse(httpRequest.responseText);
      console.log(text);

      let googleMapLink = 'https://www.google.com/maps/embed/v1/place?key=AIzaSyAcCN0jWGgLTS_Uru8xDLaZ-GxisowNuIQ&q=' + inputCity;
      
      googleMap.setAttribute('src', googleMapLink);
    } else {
      console.log('API returned an error');
  }
  };
}
button.addEventListener('click', function() {
  getPosition();
});
