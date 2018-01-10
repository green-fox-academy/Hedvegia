'use strict';

var image = document.querySelector('img');
console.log(image.getAttribute('src'));
image = image.setAttribute('src', 'https://www.google.hu/search?q=j%C3%A1vai+kancsil&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjAuO6Uxs3YAhUDZCwKHb-aBUEQ_AUICigB&biw=1366&bih=637#imgrc=53QwmpCwABFGTM:');
var link = document.querySelector('a');
link = link.setAttribute('href', 'https://www.greenfoxacademy.com/?gclid=Cj0KCQiAkNfSBRCSARIsAL-u3X_Ti4YNBukPzUOiLxrcgi5Cytuc8-9RSN9_R8-S37BaNuJ33qqdPNMaAhT6EALw_wcB');
var button = document.querySelector('.this-one');
button.innerHTML = 'Don\' click me';
