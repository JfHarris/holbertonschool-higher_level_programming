#!/usr/bin/node
// computes the number of tasks completed by user id
const request = require('request');
const urlGet = process.argv[2];
request.get(urlGet, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const users = JSON.parse(body).reduce((info, iter) => {
    if (iter.completed) {
      if (info[iter.userId]) {
        info[iter.userId]++;
      } else {
        info[iter.userId] = 1;
      }
    }
    return info;
  }, {});
  console.log(users);
});
