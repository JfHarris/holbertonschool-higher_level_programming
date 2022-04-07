#!/usr/bin/node
//script that writes a string to a file
const fs = require('fs');
const fPath = process.argv[2];
const fWrite = process.argv[3];
fs.writeFile(fPath, fWrite, 'utf8', function (error) {
  if (error) {
    console.log(error);
  }
});
