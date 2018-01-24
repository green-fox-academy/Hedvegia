'use strict';

let test = require('tape');
let anagram = require('./anagram.js');

test ('decide that two strings are Anagramms or not', function (t) {
    let actual = anagram('string', 'gnirts');
    let expected = true;

    t.equal(actual, expected);
    t.end();
});