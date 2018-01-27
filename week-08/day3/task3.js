'use strict';
let button = document.getElementsByTagName('button')[0];
let googleMap = document.getElementsByTagName('iframe')[0];
    
function getPosition() {
  let inputCity = document.getElementById('position').value;
  
  inputCity = inputCity.split(' ')
  
  let inputs = inputCity[0] + '+' + inputCity[1];
  console.log(inputCity[0]);
  console.log(inputCity[1]);
  console.log(inputs);
  
  let httpRequest = new XMLHttpRequest();

  httpRequest.open('GET', 'https://devru-latitude-longitude-find-v1.p.mashape.com/latlon.php?location=' + inputs, true);
  httpRequest.setRequestHeader('X-Mashape-Key', 'kNZCeFC5Otmsh0OnupPCIpQNkck7p18x6A3jsnHrkaW8Bpum8V');
  httpRequest.setRequestHeader('Accept', 'application/json');
  httpRequest.send();
  httpRequest.onreadystatechange = console.log;

  httpRequest.onload = function() {

    if (httpRequest.status >= 200 && httpRequest.status < 400){

      let text = JSON.parse(httpRequest.responseText);
      console.log(text);

      let dataResults = text.Results;
      console.log(dataResults);

      let latitude = dataResults.lat;
      let longitude = dataResults.lon;
      let positionNumbers = document.createElement('div');
      let top = document.querySelector('.top');

      top.appendChild(positionNumbers);

      positionNumbers.innerText = 'Latitude:' + latitude + ', Longitude:' + longitude;

      let googleMapLink = 'https://www.google.com/maps/embed/v1/place?key=AIzaSyAcCN0jWGgLTS_Uru8xDLaZ-GxisowNuIQ&q=' + inputs;
      
      googleMap.setAttribute('src', googleMapLink);
    } else {
      console.log('API returned an error');
  }
  };
}
button.addEventListener('click', function() {
  getPosition();
});
