#!/usr/bin/nodejs
const request = require('request');
const url = process.argv[2];

if (!url) {
    process.exit(1);
}
request.get(url, (err, response) => {
    if (err) {
        console.error(err.message);
        return;
    }

    console.log(`${response.statusCode}`);
});
