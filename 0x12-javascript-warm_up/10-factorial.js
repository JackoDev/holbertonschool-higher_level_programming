#!/usr/bin/node
// a script that computes and prints a factorial
function fact (n) {
  if ((isNaN(n)) || (n === 1)) {
    return 1;
  } else {
    return n * fact(n - 1);
  }
}
console.log(fact(parseInt(process.argv[2])));
