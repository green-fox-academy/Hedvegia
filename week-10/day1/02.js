'use strict';

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference

function Rectangles(firstSides, secondSides) {
    this.firstSides = firstSides;
    this.secondSides = secondSides;
}

Rectangles.prototype.getArea = function() {
    return this.firstSides * this.secondSides
}

Rectangles.prototype.getCircumference = function() {
    return this.firstSides * 2 + this.secondSides * 2;
}

let square = new Rectangles(10, 10);
console.log(square.getArea());
console.log(square.getCircumference());