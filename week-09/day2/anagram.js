'use strict';

let anagram = {

    isItAnagram: function(firstWord, secondWord) {
        let first = firstWord.split('').sort().join('');
        let second = secondWord.split('').sort().join('');
        return first == second;
    }
}

console.log(anagram.isItAnagram('aaaaaaaaab', 'baaaaaaaaa'));

module.exports = anagram.isItAnagram;