'use strict';

//1
var king = document.querySelector('#b325');
console.log(king)

//2
var conceited = document.querySelector('.b326');
alert(conceited.textContent);


//3
var businessLamp = document.querySelectorAll('.big');
console.log(businessLamp[0].textContent, businessLamp[1].textContent);


//4
var conceitedKing = document.getElementsByTagName('div');
alert(conceitedKing[0].textContent);
alert(conceitedKing[1].textContent);

//5
var noBusiness = document.getElementsByTagName('div');
console.log(noBusiness[0], '\n', noBusiness[1], '\n', noBusiness[2])

//6
var allBusiness = document.getElementsByTagName('p');
alert(allBusiness[0].textContent);