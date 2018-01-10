'use strict';

//1
var headingContent = document.getElementsByTagName('h1');
alert(headingContent[0].textContent);

//2
var firstParagraph = document.getElementsByTagName('p');
console.log(firstParagraph[0].textContent);

//3
var secondParagraph = document.querySelector('.other');
alert(secondParagraph.textContent);

//4
var headingGetNewContent = document.querySelector('h1');
headingGetNewContent.innerHTML = '<h1>New content</h1>'
console.log(headingGetNewContent.textContent);

//5
var lastParagraph = document.querySelector('.result');
lastParagraph.innerHTML = secondParagraph.textContent;
console.log(lastParagraph.textContent);