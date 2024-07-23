#!/usr/bin/nodejs
class Rectangle {
    constructor(w, h) {
        if (w <= 0 || isNaN(w)) {
            this.width = "";
        }
        else {
            this.width = w;
        }
        if (h <= 0 || isNaN(h)) {
            this.height = "";
        }
        else {
            this.height = h;
        }
}
}
module.exports = Rectangle;