#!/usr/bin/node
// class Square defines square & inherits from Rectangle of 4-rectangle
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
