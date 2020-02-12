#!/usr/bin/node
const fileStr = require('fs');
const req = require('request');
const url = process.argv[2];
req(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fileStr.writeFileSync(process.argv[3], body);
  }
});
