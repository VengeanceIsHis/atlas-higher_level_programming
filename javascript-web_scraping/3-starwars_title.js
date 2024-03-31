#!/usr/bin/nodejs
const request = require('request');

argument = process.argv[2];
movie = "https://swapi-api.hbtn.io/api/films/" + argument;

request.get(movie, (error, response, body) => {
    if (error) {
        console.error('Error:', error);
        }
    else {
        try {
            const movieData = JSON.parse(body);

            if (movieData.title) {
                console.log('Movie title:', movieData.title);
            }
        } catch (parseError) {
            console.error('Error parsing JSON:', parseError);
        }
    }
});