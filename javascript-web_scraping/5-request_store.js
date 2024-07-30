#!/usr/bin/nodejs
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filename = process.argv[3];

request.get(url, (err, response, body) => {
  if (err) {
    console.error('Error fetching the URL:', err.message);
    return;
  }

    // Write the body to the file
    fs.writeFile(filename, body, (err) => {
        if (err) {
            console.error('Error writing to file:', err.message);
        }
    });
});
