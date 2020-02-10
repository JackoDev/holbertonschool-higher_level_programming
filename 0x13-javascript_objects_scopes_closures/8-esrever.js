#!/usr/bin/node
// a function that returns the reversed version of a list.
exports.esrever = function (list) {
  const newList = [];
  const last = list.length - 1;
  for (let i = last; i >= 0; i--) {
    newList.push(list[i]);
  }
  return (newList);
};
