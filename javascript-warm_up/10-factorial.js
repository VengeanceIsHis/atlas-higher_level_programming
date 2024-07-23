#!/usr/bin/nodejs
const intvalue = parseInt(process.argv[2], 10);
function factorial (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const result = factorial(intvalue);
console.log(result);
