#!/usr/bin/nodejs
let intvalue = parseInt(process.argv[2], 10);
if (isNaN(intvalue)) {
  console.log('Not a number');
} else {
  console.log('My number:', intvalue);
}
