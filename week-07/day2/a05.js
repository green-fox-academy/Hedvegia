'use strict';

// Check if the array contains "7" if it contains print "Hoorray" otherwise print "Noooooo"

var numbers = [1,2,3,4,5,6,8];

var hasItSeven = numbers.forEach(function(element) {
    if (element == 7) {
        return 1
    } 
});

if (hasItSeven == 1) {
    console.log('Hoorray');
} else {
    console.log('Nooooo')
}
