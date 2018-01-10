'use strict';

var paragraphs = document.getElementsByTagName('p');
console.log(paragraphs);

var paragraph = paragraphs[0].textContent
paragraphs[0].textContent = paragraphs[1].textContent
paragraphs[1].textContent = paragraphs[2].textContent
paragraphs[2].textContent = paragraphs[3].textContent
paragraphs[3].textContent = paragraph

console.log(paragraphs)