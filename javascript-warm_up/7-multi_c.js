#!/usr/bin/nodejs
<<<<<<< HEAD
const args = process.argv;
const intvalue = parseInt(process.argv[2], 10);
=======
let intvalue = parseInt(process.argv[2], 10);
>>>>>>> refs/remotes/origin/master
if (isNaN(intvalue)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < intvalue; i++) {
    console.log('C is fun');
  }
}
