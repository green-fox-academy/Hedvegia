'use strict';

let pics = document.querySelectorAll('.pics');
console.log(pics);
console.log(pics[1]);
let picture = document.querySelectorAll('img')[1];
console.log(picture);
let currentIndex;

for (let i= 0; i < pics.length; i++) {
    pics[i].addEventListener('click', function(event) {
        let src = pics[i].getAttribute('src');
        console.log(src);
        picture.setAttribute('src', src);
        currentIndex = [i];
    });
}

let leftArrow = document.querySelector('.left');
let rightArrow = document.querySelector('.right');

function moveLeftThePics() {
    for (let l = 0; l < pics.length; l++){
        if (l == currentIndex) {
            let src = pics[l-1].getAttribute('src');
            console.log(src);
            picture.setAttribute('src', src);
            currentIndex = [l-1];
        }  
    }
}

function moveRightThePics() {
    for (let r = 0; r < pics.length; r++) {
        if (r == currentIndex) {
            let src = pics[r+1].getAttribute('src');
            console.log(src);
            picture.setAttribute('src', src);
            currentIndex = [r+1];
        }
    }
}

leftArrow.addEventListener('click', moveLeftThePics);
rightArrow.addEventListener('click', moveRightThePics);