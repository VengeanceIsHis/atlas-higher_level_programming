#!/usr/bin/nodejs
let args = process.argv;
let param = args[2]
if (parseInt(param))
    console.log("My number: " + param)
else
    console.log("Not a number")
