'use strict';
// Join the two array by matching one girl with one boy in the order array
// Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

var girls = ["Eve","Ashley","Bözsi","Kat","Jane"];
var boys = ["Joe","Fred","Béla","Todd","Neef","Jeff"];
var order = [];

for (var i=0; i <= girls.length; i++) {
    order.push(girls[i]);
    order.push(boys[i]);
}

if (boys.length > girls.length) {
    order.push(boys[-1]);
} else if (boys.length < girls.length) {
    order.push(girls[-1]);
}

console.log(order);
