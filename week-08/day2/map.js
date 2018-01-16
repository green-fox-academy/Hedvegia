'use strict';

var fruits = [
  'melon',
  'apple',
  'strawberry',
  'blueberry',
  'pear',
  'banana'
];

// Create a new array of consists numbers that shows how many times the 'e' letter
// occurs in the word stored under the same index at the fruits array!
// Please use the map method.

let map = fruits.map(function(item) {
    let itemList = item.slice("")
    let howManyTimes = 0 
    for (let i = 0; i < itemList.length; i++) {
        if (itemList[i] == 'e') {
            howManyTimes++
        }
    }
    return howManyTimes
});

console.log(map)