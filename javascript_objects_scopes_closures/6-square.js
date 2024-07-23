#!/usr/bin/nodejs
const BaseSquare = require('./5-square');
class Square extends BaseSquare {
    constructor(size) {
        super(size, size);
    }
    charPrint(c="X") {

        let output = "";
        for (let j = 0; j < this.size; j++)
        {
            output += c;
        }
        for (let i = 0; i < this.size; i++)
        {
            console.log(output);
        }
    }
}
module.exports = Square;