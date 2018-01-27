'use strict'

var request = new XMLHttpRequest();

request.open('GET', 'https://devru-latitude-longitude-find-v1.p.mashape.com/latlon.php?location=Budapest');
request.setRequestHeader('X-MAshape-Key', 'kNZCeFC5Otmsh0OnupPCIpQNkck7p18x6A3jsnHrkaW8Bpum8V');
request.send();
request.onload = function () {
  if (request.status >= 200 && request.status < 400) {
      let text = JSON.parse(request.responseText);
      console.log(text);
} else {
  console.log('error');
}
}