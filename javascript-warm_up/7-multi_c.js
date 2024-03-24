#!/usr/bin/nodejs
const args = process.argv;
const param = args[2];
let i = 0;
if (parseInt(param)) {
  while (i < param) {
    console.log('C is fun');
    i++;
  }
}
