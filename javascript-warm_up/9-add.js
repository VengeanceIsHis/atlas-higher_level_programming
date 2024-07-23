#!/usr/bin/nodejs
let one = parseInt(process.argv[2], 10);
let two = parseInt(process.argv[3], 10);
function add(a, b)
{
    result = a + b;
    return result
}
console.log(add(one, two))