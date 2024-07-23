#!/usr/bin/nodejs
let intvalue = parseInt(process.argv[2], 10);
if (isNaN(intvalue)) {
    console.log('Missing number of occurrences');
}
else {
    for (let i = 2; i < process.argv.length; i++)
    {
        console.log('C is fun');
    }
}