#!/usr/bin/nodejs
const fs = require('fs');
fs.appendFile(process.argv[2], process.argv[3], 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
