'use strict';

let test = require('tape');
let apple = require('./apple.js');

test ('log out apple', function (t) {
    let actual = apple.getApple();
    let expected = 'apple';

    t.equal(actual, expected);
    t.end();
});