#!/usr/bin/nodejs
const fs = require('fs');


const filepath = process.argv[2];
string = process.argv[3];

fs.appendFile(filepath, string, (err) => {
    if (err) throw err;
});