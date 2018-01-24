'use strict';

let test = require('tape');
let Summa = require('./sum.js');

test ('sum the list of numbers', function (t) {
    let actual = Summa.sum(1, 2, 3, 4, 5, 6, 7);
    let expected = '28';

    t.equal(actual, expected);
    t.end();
});