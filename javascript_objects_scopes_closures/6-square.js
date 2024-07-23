#!/usr/bin/nodejs
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
    constructor(size) {
        super(size, size);
    }
    charPrint(c="X") {
        let output = "";
        for (let j = 0; j < size; j++)
        {
            output += c;
        }
        for (let i = 0; i < size; i++)
        {
            console.log(output);
        }
    }
}
module.exports = Square;