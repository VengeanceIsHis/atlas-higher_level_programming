#!/usr/bin/nodejs
const request = require('request');


let count = 0;
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
console.log(movieData)
while (i < 7) {
    individual = argument + '/' + i;
    console.log(individual)
    request.get(individual, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    }
    else {
        const indi_movie = JSON.parse(body);
        if (indi_movie.characters.includes("https://swapi-api.hbtn.io/api/people/18/"))
        {
            console.log("This works")
            count++;
        }
    }
  });
  i++;
}
console.log(count);
