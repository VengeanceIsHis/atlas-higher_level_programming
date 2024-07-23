#!/usr/bin/nodejs
const one = parseInt(process.argv[2], 10);
const two = parseInt(process.argv[3], 10);
function add (a, b) {
  let result = a + b;
  return result;
}
console.log(add(one, two));
