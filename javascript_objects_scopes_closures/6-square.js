#!/usr/bin/node
const Square = require('./5-square');
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
    constructor(size) {
        super(size);
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