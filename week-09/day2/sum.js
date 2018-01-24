'use strict';

let Summa = {
    sum: function(a, b, c, d, e, f, g) {
        return a+b+c+d+e+f+g
    }
}

console.log(Summa.sum(1, 2, 3, 4, 5, 6, 7));

module.exports = Summa.sum;