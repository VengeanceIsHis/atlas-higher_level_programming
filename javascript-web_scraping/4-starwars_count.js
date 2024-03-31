#!/usr/bin/nodejs
const request = require('request');


const argument = process.argv[2];


request.get(argument, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    }
    else {
        const movieData = JSON.parse(body);
        while (movieData.films[i])
        {
            if (movieData.films.characters)
                console.log(movieData.films.characters)
            i++;
        }
    }
  });
