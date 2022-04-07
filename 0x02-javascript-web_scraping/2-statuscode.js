#!/usr/bin/node
const urlGet = process.argv[2];
const request = require('request');
request(urlGet, function (error, response) {
  if (error) {
    console.log(error);
    return;
  }
  console.log('code: ' + response.statusCode);
});
