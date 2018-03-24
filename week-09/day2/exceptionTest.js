'use strict';

let test = require('tape');
let exception = require('./exception.js');

test('Add two string', function (t) {
  t.equal(extend.addString('string', 'gnirts'), 'stringgnirts');
  t.end();
});

test('Add two string', function (t) {
  t.equal(extend.addString(111, 111), '111 is not a string');
  t.end();
});