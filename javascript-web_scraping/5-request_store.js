#!/usr/bin/nodejs
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file_name = process.argv[3];

request.get(url, (err, response, body) => {
    if (err) {
        console.error('Error fetching the URL:', err.message);
        return;
    }

    // Write the body to the file
    fs.writeFile(file_name, body, (err) => {
        if (err) {
            console.error('Error writing to file:', err.message);
        } else {
            console.log(`Content saved to ${file_name}`);
        }
    });
});