#!/usr/bin/nodejs
const args = process.argv;
let i = 2;
let stored = 0;
while (i < args.length) {
  if (i === 2) {
    if (parseInt(args[i]) > parseInt(args[i + 1])) {
      stored = args[i];
      i++;
    }
  }
  if (args[i] > stored) { stored = args[i]; }
}
console.log(stored);
