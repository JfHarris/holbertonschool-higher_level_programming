#!/usr/bin/node
// adding to Rectangle---If w or h == 0 or a - int, create empty obj
class Rectangle {
  constructor (w, h) {
    if (((w = parseInt(w)) && (h = parseInt(h))) > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
