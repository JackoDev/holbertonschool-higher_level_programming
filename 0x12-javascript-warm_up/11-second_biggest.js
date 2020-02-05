#!/usr/bin/node
// a script that searches the second biggest integer in the list of arguments.
function rev (a, b) {
  return b - a;
}
if (process.argv.length <= 4) {
  console.log(0);
} else {
  const argArray = [];
  const arrSlice = process.argv.slice(2);
  for (const i of arrSlice) {
    argArray.push(Number(i));
  }
  argArray.sort(rev);
  console.log(argArray[1]);
}
