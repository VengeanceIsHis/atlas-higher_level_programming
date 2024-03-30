#!/usr/bin/nodejs
const fs = require('fs');


const argument = process.argv[2];
fs.readFile(filename, 'utf-8', (err, data) => {
    if (err) {
        console.error(err);
    }
    else {
        console.log(data)
    }
});