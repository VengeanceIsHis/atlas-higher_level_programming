#!/usr/bin/nodejs
const Square = require('./5-square');
class Square {
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