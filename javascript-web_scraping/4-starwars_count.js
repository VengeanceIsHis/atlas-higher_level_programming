const request = require('request');

const apiUrl = process.argv[2];
const characterUrl = "https://swapi-api.hbtn.io/api/people/18/";

let count = 0;

function fetchFilmData(url) {
  request.get(url, (error, response, body) => {
    if (error) {
      console.error('Error fetching film data:', error);
      return;
    }

    try {
      const filmData = JSON.parse(body);
      if (filmData.characters && filmData.characters.includes(characterUrl)) {
        count++;
      }
    } catch (parseError) {
      console.error('Error parsing film data:', parseError);
    }
  });
}

function countMoviesWithWedgeAntilles(apiUrl) {
  request.get(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error fetching movie list:', error);
      return;
    }

    try {
      const movieList = JSON.parse(body);
      if (!movieList.results || !Array.isArray(movieList.results)) {
        console.error('Invalid movie list format');
        return;
      }

      movieList.results.forEach(movie => {
        fetchFilmData(movie.url);
      });

      setTimeout(() => {
        console.log(`Number of movies where "Wedge Antilles" is present: ${count}`);
      }, 1000);
    } catch (parseError) {
      console.error('Error parsing movie list:', parseError);
    }
  });
}

countMoviesWithWedgeAntilles(apiUrl);