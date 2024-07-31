
$(document).ready(function() {
    $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function(data) {
    $('#list_movies').append(data.title)
    })
})