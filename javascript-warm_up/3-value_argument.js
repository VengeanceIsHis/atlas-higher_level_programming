#!/usr/bin/nodejs
const args = process.argv.slice(2);

if (args[2])  {console.log(args[2])}
else {
    console.log("No argument")
}
