#!/usr/bin/nodejs
const Rectangle = require("./4-rectangle.js")
class Square extends Rectangle{
    contructor(size) {
        super(size, size);
    }
}