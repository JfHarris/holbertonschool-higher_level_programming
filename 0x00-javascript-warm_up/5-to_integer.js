#!/usr/bin/node
const inte = parseInt(process.argv[2]);
if (inte) {
  console.log('My number: ' + inte);
} else {
  console.log('Not a number');
}
