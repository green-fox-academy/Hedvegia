'use strict';

var paragraphs = document.getElementsByTagName('p');
if ('red-dot?', paragraphs[2].classList.contains('red-dot')) {
  alert('OMG DOTS')
} 
if ('dolphin?', paragraphs[3].classList.contains('dolphin')) {
  paragraphs[3].innerHTML = 'pear';
}
if ('apple?', paragraphs[0].classList.contains('apple')) {
  paragraphs[0].innerHTML = 'dog';
}
paragraphs[0].classList.add('red');
paragraphs[1].classList.replace('balloon', 'balloon-like');
