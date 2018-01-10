'use strict';

var fromRemove = document.querySelector('ul');
var remove = document.querySelector('li');
fromRemove.removeChild(remove);

for (var i = 1; i <= 16; i++) {
    var listElements = document.createElement('li');
    listElements.textContent = 'Empty box #' + i;
    fromRemove.appendChild(listElements);
}