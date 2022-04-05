#!/usr/bin/node
// adding to Rectangle--printing rectangle using X
class Rectangle {
  constructor (w, h) {
    if (((w = parseInt(w)) && (h = parseInt(h))) > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    console.log(
      ('X'.repeat(this.width) + '\n')
        .repeat(this.height)
        .split('')
        .slice(0, -1)
        .join('')
    );
  }
}
module.exports = Rectangle;
