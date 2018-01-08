// Crate a program that draws a chess table like this
//
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % % 
//  % % % %
//
var line = 7;

for (var i = 0; i <= line; i++) {
    if (i % 2 == 0) {
        console.log('%'.repeat(line));
    } else if (i % 2 == 1) {
        console.log(' ' + '%'.repeat(line));
    }
}