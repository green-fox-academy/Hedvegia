'use strict';
// - Create (dynamically*) a two dimensional list
//   with the following matrix**. Use a loop!
//
//   0 0 0 1
//   0 0 1 0
//   0 1 0 0
//   1 0 0 0
//
// - Print this two dimensional list to the console
//
// * size should depend on a variable
// ** Relax, a matrix is just like an array

var number = 10
var a = []

for (var i = 0; i < number; i++) {
    var b = [];
    for (var j = 0; j < number; j++) {
        if (i == j) {
            b.push(1);
        } else {
            b.push(0);
        }  
    }
    a.push(b)
}

for (var z = 0; z < number; z++) {
    console.log(a[z].reverse().join(' '));
}