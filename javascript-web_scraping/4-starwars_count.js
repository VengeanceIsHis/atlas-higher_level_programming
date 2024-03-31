#!/usr/bin/nodejs
const request = require('request');


const argument = process.argv[2];
let i = 0;
let movieData;
request.get(argument, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    }
    else {
        movieData = JSON.parse(body);
    }
});

while (i < movieData.count) {
    individual = argument + i;
    console.log(individual)
    request.get(individual, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    }
    else {
        const indi_movie = json.parse(body);
        console.log(indi_movie.characters);
    }
  });
  i++;
}
