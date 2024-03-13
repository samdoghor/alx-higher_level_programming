#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    const line = 'X';

    while (i < this.height) {
      console.log(line.repeat(this.width));
      i += 1;
    }
  }
}

module.exports = Rectangle;
