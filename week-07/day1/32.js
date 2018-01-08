'use strict';

var lineCount = 6;


// Write a program that draws a
// square like this:
//
//
// %%%%%
// %%  %
// % % %
// %  %%
// %   %
// %%%%%
//
// The square should have as many lines as lineCount is

var sideCount = lineCount - 2;
console.log('%'.repeat(lineCount))
for (var i = 0; i < sideCount; i++) {
    console.log('%' + ' '.repeat(i) + '%' + ' '.repeat(lineCount -3 -i) + '%');
}
console.log('%'.repeat(lineCount))
