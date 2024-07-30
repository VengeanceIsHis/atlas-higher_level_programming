#!/usr/bin/nodejs
const request = require('request');
const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err.message);
    return;
  }
  const result = {};
  const data = JSON.parse(body);
  data.forEach(task => {
    const { userId, completed } = task;
    if (completed) {
      if (!result[userId]) {
        result[userId] = 0;
      }
      result[userId]++;
    }
  });
  console.log(result);
});
