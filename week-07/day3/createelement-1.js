'use strict';

var asteroid = document.querySelector('ul');
var newAsteroid = document.createElement('li');
newAsteroid.textContent = 'The Green Fox';
asteroid.appendChild(newAsteroid);

var newAsteroidLamp = document.createElement('li');
newAsteroidLamp.textContent = 'The Lamplighter';
asteroid.appendChild(newAsteroidLamp);

var container = document.querySelector('.container');
var heading = document.createElement('h1');
heading.textContent = 'I can add elements to the DOM';
container.appendChild(heading);

var image = document.createElement('img');
image.setAttribute('src', 'https://static.wixstatic.com/media/f4461b_83457ca5dd844c71a760d36e6583d0ff.png/v1/fill/w_168,h_168,al_c,usm_0.66_1.00_0.01/f4461b_83457ca5dd844c71a760d36e6583d0ff.png');
container.appendChild(image);