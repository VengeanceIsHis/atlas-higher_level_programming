#!/usr/bin/nodejs
const https = require('https');
const url = process.argv[2];

https.get(url, (res) => {
    console.log('Status Code:', res.statusCode);
    });