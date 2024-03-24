#!/usr/bin/nodejs
const numofArgs = process.argv.length - 2;
if (numofArgs == 0)
    console.log("No argument")
else if (numofArgs == 1)
    console.log("Argument found")
else
    console.log("Arguments found")
