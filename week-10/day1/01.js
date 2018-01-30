'use strict';

// Create a constructor for creating Animals.
// it should take one parameter: what the animal says
// Every animal should have a method called say() that prints what the animal says

function Animal(whatTheAnimalSays) {
    this.whatTheAnimalSays = whatTheAnimalSays;
}

Animal.prototype.say = function() {
    console.log(this.whatTheAnimalSays);
}

let cat = new Animal('meow');

cat.say();