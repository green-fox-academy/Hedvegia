'use strict';

let Sum = {
    sum: function(list) {
        let sumOfNumbers = 0
        list.forEach(item => sumOfNumbers += item)
        return sumOfNumbers
    }
}

console.log(Sum.sum([1, 2, 3, 4, 5, 6, 7]));

module.exports = Sum.sum;