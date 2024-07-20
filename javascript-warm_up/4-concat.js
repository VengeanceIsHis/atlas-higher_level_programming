#!/usr/bin/nodejs
let one = ""
let two = ""
if (process.argv[2]) {
  const one = process.argv[2];
} else {
  const one = 'undefined';
}
if (process.argv[3]) {
  const two = process.argv[3];
} else {
  const two = 'undefined';
}
console.log(one, 'is', two);
