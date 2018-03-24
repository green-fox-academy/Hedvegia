'use strict';

let test = require('tape');
let exception = require('./exception.js');

test('Add two string', function (t) {
  t.equal(function() {exception.addString('string', 'gnirts'), 'stringgnirts'});
  t.end();
});

test('Add two string', function (t) {
  t.throws(function() {exception.addString(111, 111), '111 is not a string'});
  t.end();
});