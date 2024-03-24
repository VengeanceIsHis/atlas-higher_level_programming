#!/usr/bin/nodejs
const args = process.argv;
let param1 = args[2];
let param2 = args[3];
let sum = 0;
function add(a, b)
{
    sum += a;
    sum += b;
    console.log(sum);
}