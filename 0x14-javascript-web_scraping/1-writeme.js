#!/usr/bin/node
// a script that writes a string to a file.
const fileStr = require('fs');
fileStr.writeFileSync(process.argv[2], process.argv[3]);
