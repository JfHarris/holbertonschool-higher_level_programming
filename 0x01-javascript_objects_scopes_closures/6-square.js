#!/usr/bin/node
// class Square that a square & inherits from Square of 5-square.js
const SquareBase = require('./5-square');
class Square extends SquareBase {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    process.stdout.write((c.repeat(this.width) + '\n').repeat(this.height));
  }
}
module.exports = Square;
