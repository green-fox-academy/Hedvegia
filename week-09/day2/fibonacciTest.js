'use strict';

let test = require('tape');
let fibonacci = require('./fibonacci.js');

test ('log out the nth fibonacci number ', function (t) {
    let actual = fibonacci(8);
    let expected = 21;

    t.equal(actual, expected);
    t.end();
});

test ('log out the nth fibonacci number', function (t) {
    let actual = fibonacci(8);
    let expected = 23;

    t.equal(actual, expected);
    t.end();
});

test ('log out the nth fibonacci number', function (t) {
    let err = fibonacci('string');
    let msg = 'The input is not an integer';

    t.error(err, msg);
    t.end();
});