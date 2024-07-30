#!/usr/bin/nodejs
const request = require('request');
const url = process.argv[2];

request.get(url, (err, response, body) => {
<<<<<<< HEAD
  if (err) {
    console.error(err.message);
    return;
  }
  const result = {};
  const data = JSON.parse(body);
  const i = 0;
  data.forEach(task => {
    const { userId, completed } = task;

    if (!result[userId]) {
      result[userId] = 0;
    }
    if (completed) {
      result[userId] = (result[userId] || 0) + 1;
    }
  });
  console.log(result);
});
=======
    if (err) {
      console.error(err.message);
      return;
    }
    let result = {};
    const data = JSON.parse(body);
    data.forEach(task => {
        const { userId, completed } = task;

        if (!result[userId]) {
        }
            if (completed) {
                result[userId] = (result[userId] || 0) + 1;
        }
    });
    console.log(result);
});
>>>>>>> refs/remotes/origin/master
