#!/usr/bin/node
const fs = require('fs');
const f_path = process.argv[2];
fs.readFile(f_path, 'utf8', function read (error, fileInfo) {
  if (error) {
    console.log(error);
    return;
  }
  const content = fileInfo;
  console.log(content);
});
