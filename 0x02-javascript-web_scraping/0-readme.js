#!/usr/bin/node
// script that reads and prints the content of a file
const fs = require('fs');
const fPath = process.argv[2];
fs.readFile(fPath, 'utf8', function read (error, fileInfo) {
  if (error) {
    console.log(error);
    return;
  }
  const content = fileInfo;
  console.log(content);
});
