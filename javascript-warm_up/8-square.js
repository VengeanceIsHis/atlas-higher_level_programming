#!/usr/bin/nodejs
let intvalue = parseInt(process.argv[2], 10);
if (isNaN(intvalue)) {
    console.log('Missing size');
  }
for (let x = 0; x < intvalue; x++)
{
    let output = "";
    for (let y = 0; y < intvalue; y++)
    {
        output += "X"; 
    }
    console.log(output);
}
