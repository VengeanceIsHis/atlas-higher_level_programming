$(document).ready(function() {
    $('#red_header').css({
        'cursor': 'pointer',
        'border': '1px solid black',
        'padding': '10px',
        'background-color': '#e0e0e0'
    });
    $('red_header').on('click', function() {
        $('header').css('color', '#FF0000');
    });
});