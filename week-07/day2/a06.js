'use strict';
// Check if array contains all of the following elements: 4,8,12,16
// Create a 'numChecker' function that accepts 'listOfNumbers' as an input
// it should return "true" if it contains all, otherwise "false"

var listOfNumbers = [2, 4, 6, 8, 10, 12, 14, 16];

function numChecker(listOfNumbers) {
    var checker = 0
    listOfNumbers.forEach(function(items) {
        if (items == 4 || items == 8 || items == 12 || items == 16) {
            checker += 1
        } 
    });
    if (checker == 4) {
        console.log(true);
    } else {
        console.log(false);
    }
}
numChecker(listOfNumbers)