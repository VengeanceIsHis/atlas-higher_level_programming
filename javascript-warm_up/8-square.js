#!/usr/bin/nodejs
const args = process.argv;
const param = args[2];
let i = 0; let j = 0;
console.log(param)
let string = '';
let temp_string = '';
if (parseInt(param)) {
  while (i < parseInt(param)) {
    temp_string = '';
    while (j < parseInt(param)) {
      temp_string += 'X';
      j++;
    }
    console.log("bug is here");
    string = temp_string;
    console.log(string);
    i++;
  }
}
