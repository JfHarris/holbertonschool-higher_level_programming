#!/usr/bin/node
// prints title of a Star Wars movie where the ep # matches given int
const request = require('request');
const urlEnd = 'https://swapi-api.hbtn.io/api/films/';
const epNum = process.argv[2];
request(urlEnd + epNum, function (error, response, body) {
  error && console.log(error);
  console.log(JSON.parse(body).title);
});
