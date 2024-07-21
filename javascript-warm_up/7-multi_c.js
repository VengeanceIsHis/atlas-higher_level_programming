#!/usr/bin/nodejs
const args = process.argv;
let intvalue = parseint(process.argv[2], 10);
if (isNaN(intvalue)) {
    console.log('Missing number of occurrences');
}
else {
    for (let i = 2; i < args.length; i++)
    {
        console.log('C is fun');
    }
}