#!/usr/bin/node
// a script that reads and prints the content of a file.
const fileStream = require('fs');
fileStream.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
