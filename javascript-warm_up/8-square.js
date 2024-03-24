#!/usr/bin/nodejs
const args = process.argv;
const param = args[2];
let i = 0; let j = 0;
let string = '';
if (parseInt(param)) {
  while (j < parseInt(param)) {
    string += 'X';
    j++;
  }
  while (i < param) {
    console.log(string);
    i++;
  }
} else { console.log('Missing size'); }
