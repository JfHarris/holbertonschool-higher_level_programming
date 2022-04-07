#!/usr/bin/node
// gets the contents of a webpage and stores it in a file
const request = require('request');
const fs = require('fs');
const urlGet = process.argv[2];
const fPath = process.argv[3];
request.get(urlGet, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  fs.writeFile(fPath, body, 'utf8', function (error) {
    if (error) {
      console.log(error);
    }
  });
});
