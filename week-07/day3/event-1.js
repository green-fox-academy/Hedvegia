'use strict';

var button = document.querySelector('button');
var div = document.querySelector('div');
var background = document.createElement('div');
div.appendChild(background);

function turnOnTheParty(){
    background.classList.toggle('party');
}

button.addEventListener('click', turnOnTheParty);
