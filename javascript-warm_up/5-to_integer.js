#!/usr/bin/nodejs
const args = process.argv;
const param = args[2];
if (parseInt(param)) { console.log('My number: ' + param); } else { console.log('Not a number'); }
