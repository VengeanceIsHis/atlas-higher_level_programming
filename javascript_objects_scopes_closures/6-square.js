#!/usr/bin/nodejs
const BaseSquare = require('./5-square');
class Square extends BaseSquare {
    constructor(size) {
        super(size, size);
    }
    charPrint(c = "X") {

        let output = "";
        for (let j = 0; j < this.height; j++)
        {
            output += c;
        }
        for (let i = 0; i < this.height; i++)
        {
            console.log(output);
        }
    }
}
module.exports = Square;