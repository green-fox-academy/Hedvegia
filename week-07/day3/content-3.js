'use strict';

var firstP = document.querySelector('p');
console.log(firstP);
var pOutput1 = document.querySelector('.output1');
pOutput1.innerHTML = firstP.textContent;
console.log(pOutput1);
var pOutput2 = document.querySelector('.output2');
pOutput2.innerHTML = firstP.innerHTML;
console.log(pOutput2);