#!/usr/bin/nodejs
const request = require('request');

argument = process.argv[2];
movie = "https://swapi-api.hbtn.io/api/films/" + argument;
request.get(movie, (error, response) => {
    if (error) {
        console.error('Error:', error);
        }
    else {
    console.log(response.title);
    }
});