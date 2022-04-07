#!/usr/bin/node
//prints the # of movies where character “Wedge Antilles” is present
const request = require('request');
const urlGet = process.argv[2];
request(urlGet, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const results = JSON.parse(body).results;
  let counter = 0;
  for (const lists of results) {
    for (const characters of lists.characters) {
      if (characters.includes('18')) {
        counter = counter + 1;
      }
    }
  }
  console.log(counter);
});
