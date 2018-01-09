'use strict';
// - Create a variable named `aj`
//   with the following content: `[3, 4, 5, 6, 7]`
// - Reverse the order of the elements in `aj`
// 		- do it with the built in method
//		- do it with creating a new temp array and a loop
// - Print the elements of the reversed `aj`

var aj = [3, 4, 5, 6, 7];

function withBuiltInMethod(list) {
    console.log(list.reverse())
}

withBuiltInMethod(aj);

var ajj = [3, 4, 5, 6, 7];

function withLoopsAndNewArray(list) {
    let newTemp = [];
    for (var i = list.length-1; i >= 0; i--) {
        newTemp.push(list[i]);
    };
    console.log(newTemp);
}

withLoopsAndNewArray(ajj);