'use strict';

class Animal {
    constructor() {
        this.hunger = 5;
        this.thirsty = 5;
    }
    eat() {
        this.hunger -= 1;
    }
    drink() {
        this.thirsty -= 1;
    }
    play() {
        this.hunger += 1;
        this.thirsty += 1;
    }
}

class Farm {
    constructor(slots) {
        this.slots = slots;
        this.animals = [];
    }
    breed() {
        while (this.animals.length != this.slots) {
            let newAnimal = new Animal();
            this.animals.push(newAnimal);
        }
    }
    slaughter() {
        let deleteAnimal = this.animals[0];
        for (let i = 0; i < this.slots.length; i++) {
            if (deleteAnimal.hunger < this.animals[i].hunger) {
                deleteAnimal = this.animals[i]
            }
        let animalIndex = this.animals.indexOf(deleteAnimals);
        console.log(deleteAnimal);
        console.log(animalIndex);
        this.animals.splice(animalIndex, 1);
        }
    }
    printStates() {
        if (this.animals.lengt == this.slots) {
            console.log('The farm has ' + this.slots + 'living animals we are full.')
        } else if (this.animals.length < this.slots) {
            console.log('The farm has ' + this.animals.length + 'there are some empty place.')
        }
    }
    getRandomInt(max) {
        return Math.floor(Math.random() * Math.floor(max));
    }
    animalMethodes() {
        for (let i = 0; i < this.animals.length; i++) {
            let rand = this.getRandomInt(3);
            if (rand == 0) {
                this.animals[i].eat();
                console.log(this.animals[i]);
            } else if (rand = 1) {
                this.animals[i].drink();
                console.log(this.animals[i]);
            } else if (rand = 2) {
                this.animals[i].play();
                console.log(this.animals[i]);
            }
        }
    }
    progress() {
        this.animalMethodes();
        this.breed();
        this.slaughter();
        this.printStates();
    }
}

const SheepFarm = new Farm(20);
SheepFarm.breed();

console.log(SheepFarm.animals); // Should log 20 Animal objects

const button = document.querySelector('button');
button.addEventListener('click', function() {
    SheepFarm.progress()
    let paragraph = document.querySelector('p');
    paragraph.innerHTML = 'The farm has ' + SheepFarm.slots + 'sheep';
});



console.log(SheepFarm.animals);