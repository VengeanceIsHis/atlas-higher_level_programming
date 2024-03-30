#!/usr/bin/nodejs
const fs = require('fs');


const filepath = process.argv[2];
string = process.argv[3];

fs.appendFile(filepath, data, (err) => {
    if (err) throw err;
    console.log('Text appended to file');
});