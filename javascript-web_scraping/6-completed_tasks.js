#!/usr/bin/nodejs
const request = require('request');
const url = process.argv[2];

request.get(url, (err, response, body) => {
    if (err) {
      console.error(err.message);
      return;
    }
    let result = {};
    const data = JSON.parse(body);
    let i = 0;
    data.forEach(task => {
        const { userId, completed } = task;

        if (!result[userId]) {
            result[userId] = 0;
        }

        else {
            if (task.completed) {
                console.log("COMPLETED!!!");
                result[userId] = (result[userId] || 0) + 1;
            }
        }
    });
});