'use strict';

let button = document.querySelector('button');
let divElement = document.querySelector('div');
let background = document.createElement('div');
divElement.appendChild(background);

function turnOnTheParty(){
    background.classList.toggle('party');
}

button.addEventListener('click', turnOnTheParty);













