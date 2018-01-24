'use strict';

//Write a function that computes a member of the fibonacci sequence by a given index
//Create tests that covers all types of input (like in the previous workshop exercise)

let fibonacci = function(number) {
    if (typeof number !== 'number') {
        throw new Error('The input is not a number')
    }

    if (number < 2) {
        return number - 1
    } else {
        return fibonacci(number-1) + (number-2)
    }
}

try {
    fibonacci('number', 'number')
} catch (err) {
    console.log('catching error')
    console.log(err.message)
}

console.log(fibonacci(8))

module.exports = fibonacci;