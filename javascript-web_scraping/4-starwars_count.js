#!/usr/bin/nodejs
const request = require('request');
const url = process.argv[2];
const wedgeAntillesId = '18';


request.get(url, (err, response, body) => {
    if (err) {
      console.error(err.message);
      return;
    }
    const data = JSON.parse(body);
    let count = 0;

    data.results.forEach(film => {
        const hasWedgeAntilles = film.characters.some(characterUrl => {
            return characterUrl.endswith(`/${wedgeAntillesId}/`);
        });
        if (hasWedgeAntilles) {
            count++;
        }
    });
    console.log(count);
});