#!/usr/bin/nodejs
const args = process.argv;
const param1 = args[2];
const param2 = args[3];
let int_return = 0;
function add(a, b) {
  let sum = 0;
  sum += a;
  sum += b;
  return (sum);
}
int_return = add(param1. param2);
console.log(int_return)
