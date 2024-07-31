$(document).ready(function() {
    $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function(data) {
    const films = data.films;
    films.forEach(function(filmUrl) {
        $.get(filmUrl, function(filmData) {
            const listItem = $('<li>').text(filmData.title);
            $('#list_movies').append(listItem);
        })
    })
    })
})