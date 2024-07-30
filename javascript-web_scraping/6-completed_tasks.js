#!/usr/bin/nodejs
const request = require('request');
const url = process.argv[2];

request.get(url, (err, response, body) => {
    if (err) {
      console.error(err.message);
      return;
    }
    const data = JSON.parse(body);
    console.log(data);
  });
  