#!/usr/bin/nodejs
const args = process.argv;
const param1 = parseInt(args[2]);
const param2 = parseInt(args[3]);
let intReturn = 0;
let sum;
function add (a, b) {
  sum = 0;
  sum += a;
  sum += b;
  return (sum);
}
intReturn = add(param1, param2);
console.log(int_return);
