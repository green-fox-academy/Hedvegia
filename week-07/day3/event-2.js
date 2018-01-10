'use strict';

var button = document.querySelector('button');
    var result = document.getElementsByTagName('li');
    var classResult = document.querySelector('p');


function countItems() {
    classResult.classList.toggle('result');
    if ('result?', classResult.classList.contains('result')){
        classResult.textContent = result.length;
    } else {
        classResult.textContent = 'dunno :('
    }
}

button.addEventListener('click', countItems);