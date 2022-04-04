#!/usr/bin/node
function factorial (inte) {
  if (isNaN(inte)) {
    return 1;
  }
  if (inte < 0) {
    return -1;
  }
  if (inte === 0) {
    return 1;
  } else {
    return inte * factorial(inte - 1);
  }
}
console.log(factorial(process.argv[2]));
