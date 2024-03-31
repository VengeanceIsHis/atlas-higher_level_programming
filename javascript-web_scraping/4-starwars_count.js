#!/usr/bin/nodejs
const request = require('request');

let count = 0;
const argument = process.argv[2];
let i = 1;
let movieData;

if (process.argv[2] === "local" && process.argv[3] === "server")
{
  console.log(process.argv[5]);
}



const getMovieData = new Promise((resolve, reject) => {
  request.get(argument, (error, response, body) => {
    if (error) {
      reject(error);
    } else {
      resolve(JSON.parse(body));
    }
  });
});


let individualRequests = [];


while (i < 8) {
  const individual = argument + '/' + i;
  individualRequests.push(new Promise((resolve, reject) => {
    request.get(individual, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const indi_movie = JSON.parse(body);
        if (indi_movie.characters && Array.isArray(indi_movie.characters) && indi_movie.characters.includes("https://swapi-api.hbtn.io/api/people/18/")) {
          count++;
        }
        resolve();
      }
    });
  }));
  i++;
}


Promise.all([getMovieData, ...individualRequests])
  .then(() => {
    console.log(count);
  })
  .catch(error => {
    console.error('Error:', error);
  });
