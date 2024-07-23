#!/usr/bin/nodejs
class Rectangle {
    constructor(w, h) {
        if (w <= 0 || isNaN(w) || h <= 0) {
            this.height = "undefined"
            this.width = "undefined";
        }
        else {
            this.width = w;
            this.height = h;
        }
}
}
module.exports = Rectangle;