#!/usr/bin/nodejs
const args = process.argv;
const param1 = parseInt(args[2]);
if (!param1)
    console.log("1");
else
{
    function factorial(n) {
        if (n === 0 || n === 1)
            return (1);
        else
        return n * factorial(n - 1);
    }
console.log(factorial(param1));
}
