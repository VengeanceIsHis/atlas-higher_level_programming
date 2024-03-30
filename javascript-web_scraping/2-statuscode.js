#!/usr/bin/nodejs
const fs = require('fs');
const request = require('request')

const dataurl = process.argv[2];

request.get(dataurl, (error, response) => {
    if (error) {
        console.error('Error:', error);
    }
    else {
        console.log('code:', response.statusCode);
    }
});