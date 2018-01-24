'use strict';

let test = require('tape');
let Sum = require('./sum.js');

test ('sum the list of numbers', function (t) {
    let actual = Sum([1, 2, 3, 4, 5, 6, 7]);
    let expected = 28;

    t.equal(actual, expected);
    t.end();
});

test ('sum the list of numbers', function (t) {
    let actual = Sum([]);
    let expected = 0;

    t.equal(actual, expected);
    t.end();
});

test ('sum the list of numbers', function (t) {
    let actual = Sum([1]);
    let expected = 1;

    t.equal(actual, expected);
    t.end();
});

test ('sum the list of numbers', function (t) {
    let actual = Sum(null);
    let expected = null;

    t.equal(actual, expected);
    t.end();
});

test ('sum the list of numbers', function (t) {
    let actual = Sum(['string', 'string']);
    let expected = 'stringstring';

    t.equal(actual, expected);
    t.end();
});