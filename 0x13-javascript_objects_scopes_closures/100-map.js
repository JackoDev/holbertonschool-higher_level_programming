#!/usr/bin/node
// a script that imports an array and computes a new array.
const list1 = require('./100-data').list;
console.log(list1);
const finalList = list1.map(function (field, index) {
  return (field * index);
});
console.log(finalList);
