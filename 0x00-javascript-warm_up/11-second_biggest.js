#!/usr/bin/node
if (process.argv.length < 4) {
  console.log('0');
} else {
  const inte = process.argv.slice(2);
  inte.sort((a, b) => b - a);
  console.log(inte[1]);
}
