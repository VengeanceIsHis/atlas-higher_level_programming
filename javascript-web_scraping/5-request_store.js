#!/usr/bin/nodejs
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file_name = process.argv[3];

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err.message);
    return;
  }
  const data = JSON.parse(body);

  fs.writeFile(file_name, data);
});
