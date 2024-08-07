#!/usr/bin/nodejs
const args = process.argv.slice(2);

if (args.length === 0 || args.length === 1) {
  console.log('0');
} else {
  const numbers = args.map(arg => parseInt(arg, 10));
  const sortedNumbers = numbers.sort((a, b) => b - a);
  console.log(sortedNumbers[1]);
}
