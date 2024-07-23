#!/usr/bin/nodejs
const one = parseInt(process.argv[2], 10);
const two = parseInt(process.argv[3], 10);
function add (a, b) {
  const result = a + b;
  return result;
}
console.log(add(one, two));
module.exports = {
    add
};