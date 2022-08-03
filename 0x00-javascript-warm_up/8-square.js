#!/usr/bin/node
const sqChar = 'X';
const sqSize = process.argv[2];

if (parseInt(sqSize)) {
  for (let rowSq = 0; rowSq < sqSize; rowSq++) {
    console.log(sqChar.repeat(sqSize));
  }
} else {
  console.log('Missing size');
}
