#!/usr/bin/node
const strs = 'C is fun';
const inte = process.argv[2];
let x = 0;

if (parseInt(inte)) {
  while (x < inte) {
    console.log(strs);
    x++;
  }
} else {
  console.log('Missing number of occurrences');
}
