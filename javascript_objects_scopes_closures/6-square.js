#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
    constructor(size) {
        super(size, size);
    }

    charPrint(c) {
        if (c = undefined) {
            c = 'X'
        }
        if (parseInt(this.width && parseInt(this.height))) {
            while (j < parseInt(this.width)) {
              string += c;
              j++;
            }
      
            while (i < parseInt(this.height)) {
              console.log(string);
              i++;
            }
          }
    }
}

module.exports = Square;