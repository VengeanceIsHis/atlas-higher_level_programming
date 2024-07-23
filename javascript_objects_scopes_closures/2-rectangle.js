#!/usr/bin/nodejs
class Rectangle {
    constructor(w, h) {
        if (w <= 0 || isNaN(w) || h <= 0) {
            pass;
        }
        else {
            this.width = w;
            this.height = h;
        }
}
}
module.exports = Rectangle;