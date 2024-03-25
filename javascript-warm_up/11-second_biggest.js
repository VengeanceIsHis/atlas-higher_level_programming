#!/usr/bin/nodejs
const args = process.argv;
let i = 2;
let stored = 0;
while (i < args.length) {
  const currentNumber = parseInt(args[i])
    if (currentNumber > stored) {
      stored = currentNumber
    }
    i++;
    }
console.log(stored);
