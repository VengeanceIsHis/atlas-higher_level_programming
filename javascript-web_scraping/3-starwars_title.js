#!/usr/bin/nodejs
const request = require('request');

const argument = process.argv[2];
const movie = "https://swapi-api.hbtn.io/api/films/" + argument;

request.get(movie, (error, response, body) => {
    if (error) {
        console.error('Error:', error);
        }
    else {
        try {
            const movieData = JSON.parse(body);

            if (movieData.title) {
                console.log(movieData.title);
            }
        } catch (parseError) {
            console.error('Error parsing JSON:', parseError);
        }
    }
});