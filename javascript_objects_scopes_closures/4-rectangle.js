#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !(h) || !(w)) {
      return 'Rectangle {}';
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    let j = 0;
    let string = '';

    if (parseInt(this.width && parseInt(this.height))) {
      while (j < parseInt(this.width)) {
        string += 'X';
        j++;
      }

      while (i < parseInt(this.height)) {
        console.log(string);
        i++;
      }
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
