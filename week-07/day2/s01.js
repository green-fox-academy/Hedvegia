'use strict';

var example = "In a dishwasher far far away";

// I would like to replace "dishwasher" with "galaxy" in this example
// Please fix it for me!
// Expected ouput: In a galaxy far far away

var newWord = "galaxy"
var example = example.slice(0, 5) + newWord + example.slice(15)

console.log(example)