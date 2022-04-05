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

  rotate () {
    // exchanges the width and the height of the rectangle
    this.width += this.height;
    this.height = this.width - this.height;
    this.width -= this.height;
  }

  double () {
    // multiples the width and the height of the rectangle by 2
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
